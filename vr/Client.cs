using UnityEngine;

public class Client : MonoBehaviour{
  private Requester _requester;

  private void Start(){
    _requester = new Requester();
    _requester.Start();
  }

  private void onDestroy(){
    _requester.Stop();
  }

}
