#!/usr/bin/python3

from kafka import KafkaConsumer
import MQData_pb2 as MQData # The class file you just compiled
import json

# decoder of Elkeid PB, input string and will dump json for you.
def pbDecoder(value):
    ret = {}
    aMQData = MQData.MQData();
    aMQData.ParseFromString(value)

    # common part of message
    ret["data_type"] = str(aMQData.data_type)
    ret["timestamp"] = str(aMQData.timestamp)
    ret["agent_id"] = aMQData.agent_id
    ret["in_ipv4_list"] = aMQData.in_ipv4_list
    ret["ex_ipv4_list"] = aMQData.ex_ipv4_list
    ret["in_ipv6_list"] = aMQData.in_ipv6_list
    ret["ex_ipv6_list"] = aMQData.ex_ipv6_list
    ret["hostname"] = aMQData.hostname
    ret["version"] = aMQData.version
    ret["product"] = aMQData.product
    ret["time_pkg"] = str(aMQData.time_pkg)
    ret["psm_name"] = aMQData.psm_name
    ret["psm_path"] = aMQData.psm_path
    ret["tags"] = aMQData.tags

    # major data part of message
    for key in aMQData.body.fields:
        ret[key] =  aMQData.body.fields[key]
    
    return json.dumps(ret)


# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('hids_svr',
group_id='test',
auto_offset_reset='latest',
bootstrap_servers=['10.130.12.22:9092'],
security_protocol='SASL_PLAINTEXT',
sasl_mechanism='PLAIN',
sasl_plain_username='admin',
sasl_plain_password='elkeid',
value_deserializer = lambda m: pbDecoder(m))

# Print all message in JSON format
# this is the part that you need to code to your job
for message in consumer:
    # do something with message.value
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,message.offset, message.key,message.value))
