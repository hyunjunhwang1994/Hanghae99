public class Bus extends PublicTransport{

    int currentPassengers = 1;
    int maxPassengers = 30;
    int fare = 1000;
    int number;
    boolean status;

    int gasMileage;

    public Bus(int number) {
        this.status = true;
        super.number = number;
        System.out.println(number + "번 버스객체 만들어짐!");

    }

    @Override
    public void startDriving() {


        while (super.gasStatus > 0){

            gasMileage--;

            if(gasMileage == 0){
                super.gasStatus--;
                super.getGasStatus();
                gasMileage=50;
            }

        }

    }

    @Override
    public void boardingPassengers(int passengersNumber) {


        if(passengersNumber > (maxPassengers - currentPassengers)  ){
            System.out.println("최대 승객 수를 초과했습니다.");
        }else{

            currentPassengers += passengersNumber;

            System.out.println("탑승 승객 수 = " + passengersNumber);
            System.out.println("잔여 승객 수 = " + (maxPassengers - currentPassengers));
            System.out.println("요금 확인 = " + fare * passengersNumber);




        }




    }

    @Override
    public void bill() {

    }

    @Override
    public void boardingPassengers(int passengersNumber, String destination, int distance) {

    }
}
