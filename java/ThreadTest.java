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
            //�����м��飬�ᷢ�ִ�ӡ��˳��ͬ
            //�̵߳�ִ�У������ǰ��ճ���д�����Ⱥ�˳��
            //���ǿ�˭��ռ��CPU��˭��ִ��
            t.start();
            t2.start();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
