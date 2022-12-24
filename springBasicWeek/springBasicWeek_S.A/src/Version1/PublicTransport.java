package Version1;

public abstract class PublicTransport {

    int number;
    int gasStatus = 100;
    int currentSpeed = 0;
    boolean status = true;



    public void startDriving (){
        System.out.println("운행을 시작합니다.");

    }

    public int getGasStatus() {
        System.out.println("주유량 : " + this.gasStatus);
        if(this.gasStatus < 10){
            System.out.println("주유가 필요합니다.");
        }
        return this.gasStatus;
    }

    public void setGasStatus(int gasStatus) {
        this.gasStatus = this.gasStatus + gasStatus;


    }

    public void setChangeSpeed(int changeSpeed){
        System.out.println("속도가 변경 됩니다.");
        this.currentSpeed = changeSpeed;

    }

    public void setStatus(boolean status) {
        // true: 운행, false: 차고지행
        this.status = status;



    }

    public int getNumber() {
        return number;
    }



    public boolean isStatus() {
        if(this.status == true){
            System.out.println("상태 = 운행");
        }else{
            System.out.println("상태 = 차고지행");

        }
        return status;
    }

    public void boardingPassengers(int passengersNumber){
        // 하위클래스의 최대 탑승수에 따라 오버라이딩하기

    }

    public abstract void bill();


    public abstract void boardingPassengers(int passengersNumber, String destination,
                                            int distance);
}
