package sec09;

public class Anonymous {

    Person field = new Person(){
      void work(){
          System.out.println("출근합니다.");
      }

      @Override
      void wake(){
          System.out.println("6시에 일어납니다.");
          work();
      }






    };






}
