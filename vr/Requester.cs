using AsyncIO;
using NetMQ;
using NetMQ.Sockets;
using UnityEngine;

public class Requester : RunnableThread {

  protected override void Run(){
    ForceDotNet.Force(); //apparently this line is needed
    using (RequestSocket client = new RequestSocket()){
      client.Connect("tcp://localhost:5555");

      byte message = 255;
      bool received = false;

      while (Running){
        //TODO: action here?
        received = client.TryReceiveFrameBytes(out message);
        if(received){
          break; //escapes the running sequence
        }
      }

      //TODO: do something with the binary message?

    NetMQConfig.Cleanup(); //apparently this line is also needed
  }


}
