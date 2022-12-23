public class Taxi extends PublicTransport{

    int currentPassengers = 1;
    int maxPassengers = 5;

    int basicFare = 3000;
    int fare = 0;
    int myMoney = 0;

    boolean status;

    int gasMileage;


    public Taxi (int number) {
        this.status = true;
        super.number = number;
        System.out.println(number + "번 택시객체 만들어짐!");

    }



    @Override
    public int getGasStatus() {
        return super.getGasStatus();
    }

    @Override
    public void setGasStatus(int gasStatus) {
        super.setGasStatus(gasStatus);
    }

    @Override
    public void setChangeSpeed(int changeSpeed) {
        super.setChangeSpeed(changeSpeed);
    }

    @Override
    public void setStatus(boolean status) {
        super.setStatus(status);
    }

    @Override
    public int getNumber() {
        return super.getNumber();
    }

    @Override
    public boolean isStatus() {
        if(this.status == true){
            System.out.println("상태 = 운행");
        }else{
            System.out.println("상태 = 운행불가");

        }
        return status;
    }

    @Override
    public void bill(){


        if(getGasStatus() <= 0){
            setStatus(false);
            isStatus();
            System.out.println("누적 요금 =" + myMoney);

        }else {

            myMoney += fare;
            currentPassengers=1;

            System.out.println("누적 요금 =" + myMoney);
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
    public void boardingPassengers(int passengersNumber, String destination,
                                   int distance) {

        if(passengersNumber > (maxPassengers - currentPassengers)  ){
            System.out.println("최대 승객 수를 초과했습니다.");
        }else{

            currentPassengers += passengersNumber;

            System.out.println("탑승 승객 수 = " + passengersNumber);
            System.out.println("잔여 승객 수 = " + (maxPassengers - currentPassengers));
            System.out.println("기본 요금 확인 = " + basicFare);

            if(destination.equals("서울역")){
                fare = basicFare + 1000;

                System.out.println("목적지 = " + destination);
                System.out.println("목적지까지 거리 =" + distance);
                System.out.println("지불할 요금 =" + fare);




            }else if(destination.equals("구로디지털단지역")){
                fare = basicFare + 11000;

                System.out.println("목적지 = " + destination);
                System.out.println("목적지까지 거리 =" + distance);
                System.out.println("지불할 요금 =" + fare);



            }



        }




    }
}
