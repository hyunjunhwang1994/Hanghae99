package sec13.exam01;

import java.util.ArrayList;
import java.util.List;

public class ArrayListExample {


    public static void main(String[] args) {

        // ArrayList
        List<String> list = new ArrayList<>();

        list.add("Java");
        list.add("JDBC");
        list.add("Servlet/JSP");
        list.add(2, "Database");
        list.add("iBATIS");

        int size = list.size();
        System.out.println("총 객체수: " + size);

        String skill = list.get(2);
        System.out.println("2: " + skill);

        for(int i = 0; i<list.size(); i++){
            String str = list.get(i);
            System.out.println(i + ":"+str);
        }






    }

}
