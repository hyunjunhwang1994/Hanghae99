package Version2_Interface;


public class Bus implements PublicTransport{

    int number;
    int gasStatus = 100;
    int currentSpeed = 0;
    boolean status = true;

    int currentPassengers = 0;
    int maxPassengers = 30;
    int fare = 1000;
    int gasMileage;



    public Bus(int number) {
        System.out.println(number+"번 버스객체 만들어짐!");
        this.number = number;
    }

    @Override
    public void boardingPassengers(int passengers) {

        if (passengers > (maxPassengers - currentPassengers)) {
            System.out.println("최대 승객 수를 초과했습니다.");
            return;
        }

        this.currentPassengers += passengers;
        System.out.println("탑승 승객 수 = " + currentPassengers);
        System.out.println("잔여 승객 수 = " + (maxPassengers - currentPassengers));
        System.out.println("요금 확인 = " + fare * passengers);

    }

    @Override
    public void fillUp(int amount) {
        this.gasStatus += amount;
    }

    @Override
    public void showFill() {
        System.out.println("주유량 = " + this.gasStatus);

        if(this.gasStatus <= 5){
            status = false;
            System.out.println("주유가 필요합니다.");
        }

    }

    @Override
    public void changeStatus() {

        if(status == true){
            this.status = false;
        }else{
            this.status= true;
        }
    }

    @Override
    public void showStatus() {

        if(status==true){
            System.out.println("상태 = 운행중");

        }else {
            System.out.println("상태 = 차고지행");
        }
    }


}
