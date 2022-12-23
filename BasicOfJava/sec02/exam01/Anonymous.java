package sec02.exam01;

// anonymous class

public class Anonymous {

    // 필드 초기값으로 익명 객체 대입
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


    void method1(){
        //로컬 변수값으로 익명 객체 대입
        Person localVar = new Person(){
          void walk(){
              System.out.println("산책합니다.");
          }

          @Override
          void wake(){
              System.out.println("7시에 일어납니다.");
              walk();
          }

        };

        localVar.wake();

    }

            // 매개값으로 익명 객체 대입
    void method2(Person person){
        person.wake();
    }




}
