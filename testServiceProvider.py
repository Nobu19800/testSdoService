#!/usr/bin/env python
# -*- coding: euc-jp -*-



import sys

import RTC
import OpenRTM
import OpenRTM_aist
import TestModule, TestModule__POA
import CORBA
import SDOPackage


class testService_i(TestModule__POA.testService):
  def __init__(self):
    pass
  def echo(self, s):
    print "provider ",s
    return s

def main():
  orb = CORBA.ORB_init(sys.argv)
  poa = orb.resolve_initial_references("RootPOA")
  poa._get_the_POAManager().activate()
  
  servant = testService_i()
  oid = poa.servant_to_id(servant)
  provider = poa.id_to_reference(oid)


  compname = "corbaname::localhost:2809/NameService#TestComp0.rtc"
  robj = orb.string_to_object(compname)
  rtc = robj._narrow(RTC.RTObject)
  config = rtc.get_configuration()
  properties = []
  id = OpenRTM_aist.toTypename(servant)
  sprof = SDOPackage.ServiceProfile("test_id", id,
                                    properties, provider)
  ret = config.add_service_profile(sprof)
  sys.stdin.readline()
  ret = config.remove_service_profile("test_id")

if __name__ == '__main__':
  main()
