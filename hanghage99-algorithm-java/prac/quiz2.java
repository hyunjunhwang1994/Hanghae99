package prac;

public class quiz2 {
    public void solution(int star) {


        // 코드 작성

        for(int i=0; i<star; i++){

            for(int j=1; j<star-i; j++){
                System.out.print(" ");
            }
            for (int j=0; j<i*2+1; j++){
                System.out.print("*");
            }

            System.out.println();

        }

    }

    public static void main(String[] args) {
        quiz2 method = new quiz2();
        int star = 20;
        method.solution(star);
    }
}
