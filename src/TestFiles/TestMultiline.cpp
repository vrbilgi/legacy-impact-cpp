///////////////////////////////////////////////////////////////////////////
DequeueAction Test_Calss::dequeueCallback(Message& msg)
{
  /*
   * MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   * MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
  * MMMI$$$$$$$$$ZZZZZZZZZZZZZZZZZZZOOOOM$MM
   * MMI$$$$$$$$ZZZZZZZZZZZZZZZZZZZZOOOOOOM$M
   * MM?77$$$$$$$$$$$$ZZZZZZZZZZZZOOOOOOOO87M
   * MMZ$$7777777777777$$$$$777777777777$7$IM
   * MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   * MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   */
  try
  {
    std::string theMessageAsString;
    }
  NGI_SUPERCATCH_ACT_L("unexpected exception in first callback", _aSC = NULL;
                       return DequeueAction::MOVE_TO_EXCEPTION_QUEUE;);
}
