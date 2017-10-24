import csv
#import codecs

class Firewall:
    def __init__(self,csv_filepath):
        #load the data from csv
        #Assuming data provided is in Ascii.Hence not handling encoding/decoding of csv data 
        with open(csv_filepath) as f:
            reader = csv.reader(f)
            self.content = list(reader)
        self.inbound = {"tcp":{"port":[],"ip":[]},
                        "udp":{"port":[],"ip":[]}}
        self.outbound = {"tcp":{"port":[],"ip":[]},
                        "udp":{"port":[],"ip":[]}}
        #print sorted(self.content)
        for row in self.content:
      #https://stackoverflow.com/questions/28814603/python-convert-string-to-existing-dict-name-to-add-key-value-pairs
            #print unicode(row[2], "utf-8")
            availablePortRules =  eval("self."+row[0])[row[1]]["port"]
            self.reGeneratePortRules(availablePortRules,str(row[2]))
            eval("self."+row[0])[row[1]]["port"] = availablePortRules
            
            availableIpRules =  eval("self."+row[0])[row[1]]["ip"]
            self.reGenerateIpRules(availableIpRules,row[3]) 
            eval("self."+row[0])[row[1]]["ip"] = availableIpRules
          
            

    def accept_packet(self,bound,protocol,port,ipaddress):
        portRules =  eval("self."+bound)[protocol]["port"] 
        ipRules = eval("self."+bound)[protocol]["ip"]
        ip_address = self.convertIpToString(ipaddress)
        return self.checkPacketRules(portRules,int(port)) and self.checkPacketRules(ipRules,int(ip_address))
    
    def checkPacketRules(self,rules,target):
        for i in rules:
                if type(i) is tuple:
                    if(target>=i[0] and target<=i[1]):
                        return True
                elif i == target:
                    return True
        return False

    def convertIpToString(self,ip):
        ip_address = ''
        for i in ip.split('.'):
                ip_address += "%03d" % int(i)
        return ip_address

    def reGeneratePortRules(self,availablePortRules,port):
        if '-' in port:
            availablePortRules.append((int(port.split('-')[0]),int(port.split('-')[1])))
        else:
            port_num = int(port)
            if(self.checkPacketRules(availablePortRules,port_num)):
                return
            availablePortRules.append(port_num)
        availablePortRules.sort(key=lambda x: x[0] if type(x)=='tuple' else None)
        #Add Merge Ranges Code if time permits
            

    def reGenerateIpRules(self,availableIpRules,ip):
        ip_address = ''
        ip_address_low = ''
        ip_address_high = ''
        #print ip
        if '-' not in ip:
            for i in ip.split('.'):
                ip_address += "%03d" % int(i)
                
            ip_address = int(ip_address)
            #print ip_address
            if(self.checkPacketRules(availableIpRules,ip_address)):
                return
            availableIpRules.append(ip_address)
        else:
            for i in ip.split('-')[0].split('.'):
                    ip_address_low += "%03d" % int(i)
            for i in ip.split('-')[1].split('.'):
                    ip_address_high += "%03d" % int(i)
            availableIpRules.append((int(ip_address_low),int(ip_address_high)))
            #handle merge if time permits


if __name__ == '__main__':
    f = Firewall('test.csv')
    print f.accept_packet('inbound','udp','53','192.168.2.3')