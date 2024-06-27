def calculate_packets_transmitted(events):
    num_packets_transmitted = 0
    start_time = None
    end_time = None
    
    for event in events:
        timestamp, event_type, event_details = event
        
        if "+ " in event_type:  # Début d'une transmission
            start_time = float(timestamp)
        
        elif "- " in event_type and start_time is not None:  # Fin de la transmission
            end_time = float(timestamp)
            num_packets_transmitted += 1
        
            # Réinitialiser pour la prochaine transmission
            start_time = None
            end_time = None
    
    return num_packets_transmitted

# Exemple d'utilisation avec vos événements extraits
events = [
    ("15.0176", "+ 15.0176 /NodeList/1/DeviceList/1/$ns3::CsmaNetDevice/TxQueue/Enqueue", "ns3::EthernetHeader ( length/type=0x806, source=00:00:00:00:00:04, destination=ff:ff:ff:ff:ff:ff) ns3::ArpHeader (request source mac: 00-06-00:00:00:00:00:04 source ipv4: 172.16.1.2 dest ipv4: 172.16.1.1) Payload (size=18) ns3::EthernetTrailer (fcs=0)"),
    ("15.0176", "- 15.0176 /NodeList/1/DeviceList/1/$ns3::CsmaNetDevice/TxQueue/Dequeue", "ns3::EthernetHeader ( length/type=0x806, source=00:00:00:00:00:04, destination=ff:ff:ff:ff:ff:ff) ns3::ArpHeader (request source mac: 00-06-00:00:00:00:00:04 source ipv4: 172.16.1.2 dest ipv4: 172.16.1.1) Payload (size=18) ns3::EthernetTrailer (fcs=0)"),
    ("15.0197", "r 15.0197 /NodeList/2/DeviceList/0/$ns3::CsmaNetDevice/MacRx", "ns3::EthernetHeader ( length/type=0x806, source=00:00:00:00:00:04, destination=ff:ff:ff:ff:ff:ff) ns3::ArpHeader (request source mac: 00-06-00:00:00:00:00:04 source ipv4: 172.16.1.2 dest ipv4: 172.16.1.1) Payload (size=18) ns3::EthernetTrailer (fcs=0)"),
    ("15.0197", "+ 15.0197 /NodeList/2/DeviceList/0/$ns3::CsmaNetDevice/TxQueue/Enqueue", "ns3::EthernetHeader ( length/type=0x806, source=00:00:00:00:00:03, destination=00:00:00:00:00:04) ns3::ArpHeader (reply source mac: 00-06-00:00:00:00:00:03 source ipv4: 172.16.1.1 dest mac: 00-06-00:00:00:00:00:04 dest ipv4: 172.16.1.2) Payload (size=18) ns3::EthernetTrailer (fcs=0)"),
    ("15.0197", "- 15.0197 /NodeList/2/DeviceList/0/$ns3::CsmaNetDevice/TxQueue/Dequeue", "ns3::EthernetHeader ( length/type=0x806, source=00:00:00:00:00:03, destination=00:00:00:00:00:04) ns3::ArpHeader (reply source mac: 00-06-00:00:00:00:00:03 source ipv4: 172.16.1.1 dest mac: 00-06-00:00:00:00:00:04 dest ipv4: 172.16.1.2) Payload (size=18) ns3::EthernetTrailer (fcs=0)"),
    ("15.0218", "r 15.0218 /NodeList/1/DeviceList/1/$ns3::CsmaNetDevice/MacRx", "ns3::EthernetHeader ( length/type=0x806, source=00:00:00:00:00:03, destination=00:00:00:00:00:04) ns3::ArpHeader (reply source mac: 00-06-00:00:00:00:00:03 source ipv4: 172.16.1.1 dest mac: 00-06-00:00:00:00:00:04 dest ipv4: 172.16.1.2) Payload (size=18) ns3::EthernetTrailer (fcs=0)"),
    ("15.0218", "+ 15.0218 /NodeList/1/DeviceList/1/$ns3::CsmaNetDevice/TxQueue/Enqueue", "ns3::EthernetHeader ( length/type=0x800, source=00:00:00:00:00:04, destination=00:00:00:00:00:03) ns3::Ipv4Header (tos 0x0 DSCP Default ECN Not-ECT ttl 63 id 0 protocol 17 offset (bytes) 0 flags [none] length: 1028 10.1.1.1 > 172.16.1.1) ns3::UdpHeader (length: 1008 49153 > 80) Payload (size=1000) ns3::EthernetTrailer (fcs=0)"),
    ("15.0218", "- 15.0218 /NodeList/1/DeviceList/1/$ns3::CsmaNetDevice/TxQueue/Dequeue", "ns3::EthernetHeader ( length/type=0x800, source=00:00:00:00:00:04, destination=00:00:00:00:00:03) ns3::Ipv4Header (tos 0x0 DSCP Default ECN Not-ECT ttl 63 id 0 protocol 17 offset (bytes) 0 flags [none] length: 1028 10.1.1.1 > 172.16.1.1) ns3::UdpHeader (length: 1008 49153 > 80) Payload (size=1000) ns3::EthernetTrailer (fcs=0)"),
    ("15.0255", "r 15.0255 /NodeList/2/DeviceList/0/$ns3::CsmaNetDevice/MacRx", "ns3::EthernetHeader ( length/type=0x800, source=00:00:00:00:00:04, destination=00:00:00:00:00:03) ns3::Ipv4Header (tos 0x0 DSCP Default ECN Not-ECT ttl 63 id 0 protocol 17 offset (bytes) 0 flags [none] length: 1028 10.1.1.1 > 172.16.1.1) ns3::UdpHeader (length: 1008 49153 > 80) Payload (size=1000) ns3::EthernetTrailer (fcs=0)"),
]

num_packets = calculate_packets_transmitted(events)
print(f"Nombre de paquets transmis : {num_packets}")

