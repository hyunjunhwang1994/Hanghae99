package sec02.exam02;

public class Anonymous {
    //필드 초기값으로 대입
    RemoteControl field = new RemoteControl() {
        @Override
        public void turnOn() {
            System.out.println("TV를 켭니다.");
        }

        @Override
        public void turnOff() {
            System.out.println("TV를 끕니다.");
        }
    };


    // 로컬 변수값으로 대입
    void method1(){

        RemoteControl localVar = new RemoteControl() {
            @Override
            public void turnOn() {
                System.out.println("Audio를 켭니다.");

            }

            @Override
            public void turnOff() {
                System.out.println("Audio를 끕니다.");
            }
        };
        localVar.turnOn();

    }



    void method2(RemoteControl rc){
        rc.turnOn();
    }

}
