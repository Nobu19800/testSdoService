#!/usr/bin/env python
# -*- coding: euc-jp -*-



import sys

import RTC
import OpenRTM
import OpenRTM_aist
import TestModule, TestModule__POA


class testServiceConsumer(OpenRTM_aist.SdoServiceConsumerBase):
  
  def __init__(self):
    self._rtobj = None
    self._profile = None
    self._observer = OpenRTM_aist.CorbaConsumer(interfaceType=TestModule.testService)
    
    return


  
  def __del__(self):
    return


  def init(self, rtobj, profile):
    if not self._observer.setObject(profile.service):
      return False
    self._rtobj = rtobj
    self._profile = profile
    postclistener_ = OpenRTM_aist.PostComponentActionListenerType
    self._rtobj.addPostComponentActionListener(postclistener_.POST_ON_EXECUTE, self.onActivated)
    return True


  def onActivated(self, ec_id, ret):
      print "consumer ",self._observer._ptr().echo("test")
      return

  def reinit(self, profile):
    
    self._profile= profile
    
    return True




def testServiceConsumerInit(mgr=None):
  factory = OpenRTM_aist.SdoServiceConsumerFactory.instance()
  factory.addFactory(TestModule.testService._NP_RepositoryId,
                     testServiceConsumer,
                     OpenRTM_aist.Delete)
  return
