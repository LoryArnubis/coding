public class ThreadTest implements Runnable {

    int num = 0;

    public ThreadTest(int num){
        this.num = num;
    }
    public void run() {
            System.out.println("I'm running!" + num);
    }

    public static void main(String[] args){
        try{
            ThreadTest tt = new ThreadTest(2);
            Thread t = new Thread(tt);
            ThreadTest tt2 = new ThreadTest(4);
            Thread t2 = new Thread(tt2);
            System.out.println("main process");
            //多运行几遍，会发现打印的顺序不同
            //线程的执行，并不是按照程序写的有先后顺序
            //而是看谁抢占到CPU，谁就执行
            t.start();
            t2.start();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
