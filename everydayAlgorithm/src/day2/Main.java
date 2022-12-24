package day2;


import java.util.Stack;

public class Main {

    // 2022 12월 24일
    // https://school.programmers.co.kr/learn/courses/30/lessons/12909
    // 스택 자료구조 활용 올바른 괄호 찾기


    boolean solution(String s) {
        boolean answer = true;

        Stack<Character> characters = new Stack<>();


        for(int i=0; i<s.length(); i++){
            if(s.charAt(i) == '('){
                characters.push('(');
            }else{
                if(characters.isEmpty()) return false;

                else characters.pop();
            }

        }
        answer = (characters.isEmpty()) ? true : false;

        return answer;
    }


    public static void main(String[] args) {


        Main test = new Main();

        System.out.println(test.solution("(())"));


    }





}
