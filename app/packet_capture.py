import threading, time, queue
from scapy.all import sniff, IP, TCP, UDP, Raw
import math
packet_queue = queue.Queue()

def extract_features(pkt):
    features = {'pkt_len': len(pkt), 'protocol':0, 'src_port':0, 'dst_port':0, 'flags':0, 'ttl':0, 'entropy':0.0}
    try:
        if IP in pkt:
            ip = pkt[IP]
            features['ttl'] = ip.ttl
            features['protocol'] = int(ip.proto)
        if TCP in pkt:
            tcp = pkt[TCP]
            features['src_port'] = int(tcp.sport)
            features['dst_port'] = int(tcp.dport)
            features['flags'] = int(tcp.flags)
        elif UDP in pkt:
            udp = pkt[UDP]
            features['src_port'] = int(udp.sport)
            features['dst_port'] = int(udp.dport)
        if Raw in pkt:
            payload = bytes(pkt[Raw].load)
            if len(payload)>0:
                freq={}
                for b in payload:
                    freq[b]=freq.get(b,0)+1
                ent=0.0
                for v in freq.values():
                    p=v/len(payload)
                    ent-=p*(0 if p==0 else math.log2(p))
                features['entropy']=ent
    except Exception:
        pass
    return features

def start_sniff(interface=None, filter=None):
    def _handle(pkt):
        feats=extract_features(pkt)
        packet_queue.put({'features':feats,'ts':time.time()})
    sniff_kwargs={'prn':_handle,'store':False}
    if interface: sniff_kwargs['iface']=interface
    if filter: sniff_kwargs['filter']=filter
    t=threading.Thread(target=lambda: sniff(**sniff_kwargs), daemon=True)
    t.start()
    return t
