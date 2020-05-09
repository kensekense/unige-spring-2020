using System.Threading;

//TODO: runnable thread should just be coms setup.

public abstract class RunnableThread {

  private readonly Thread _runnerThread;

  protected RunnableThread(){
    _runnerThread = new Thread(Run);
  }

  protected bool Running {
    get;
    private set;
  }

  protected abstract void Run();

  public void Start(){ //TODO: do we need something else here?
    Running = true;
    _runnerThread.Start();
  }

  public void Stop(){
    Running = false;
    _runnerThread.join();
  }

}
