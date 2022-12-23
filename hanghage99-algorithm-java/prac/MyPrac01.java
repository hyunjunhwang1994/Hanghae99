package prac;

public class MyPrac01 {

    public int solution(int N, int minNum, int maxNum){


        // N을 minNum혹은 maxNum으로 나누었을때 몫이 적은 경우의수 찾기
        // ex) 5와 7로 나누었을때 완벽하게 0으로 나머지가 안나온다면 -1 리턴

        int quotient = N/maxNum;
        int remainder = N%maxNum;
        int temp = 0;


        if(N%maxNum == 0){
            return -1;
        }


        int i=0;
        while (true){
            temp = maxNum * (quotient - i);

            System.out.println("temp = " + temp);
            if(temp < 0){
                return -1;
            }

            temp = N - temp;




            if((temp%minNum) != 0){
                i++;
                continue;
            }

            if(temp % minNum == 0){
                System.out.println(minNum + "의 몫 : " + (temp/minNum));
                System.out.println(maxNum + "의 몫 : " + (quotient-i));
                return (quotient-i) + (temp/minNum);
            }


        }


    }

    public static void main(String[] args) {

        int N = 3029;

        // minNum < maxNum
        int minNum = 4;
        int maxNum = 7;
        MyPrac01 prac01 = new MyPrac01();


        System.out.println(prac01.solution(N, minNum, maxNum));



    }






}
