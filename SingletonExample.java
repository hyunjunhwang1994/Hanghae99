public class SingletonExample {

    public static void main(String[] args) {


        Singleton obj1 = Singleton.getInstance();
        Singleton obj2 = Singleton.getInstance();


        System.out.println("obj1 주소 : " + obj1);
        System.out.println("obj2 주소 : " + obj2);



    }

}
