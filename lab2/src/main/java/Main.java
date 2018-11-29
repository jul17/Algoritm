import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        PainterManager painterManager = new PainterManager();
        List<Integer> countOfBigBorders = createCountOfBigBorders();


        if(painterManager.countOfPainters < countOfBigBorders.size()) {
            countOfBigBorders = painterManager.getBigbordersForPainters(countOfBigBorders);
        }
        int result = painterManager.getMaxTime(countOfBigBorders);
        System.out.println("RESULT:");
        System.out.println(result);
    }

    static List<Integer> createCountOfBigBorders(){
        List<Integer> countOfBigBorders = new ArrayList<Integer>();
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter bidBords size:  ");
        int currentBourd = 1;
        while(currentBourd>0) {
            System.out.print("Enter for :" + currentBourd + " ");
            String value = scan.nextLine();
            if(value.equalsIgnoreCase("Stop")){
                currentBourd = 0;
            }else{
                currentBourd++;
                countOfBigBorders.add(Integer.parseInt(value.trim()));
            }
        }
        return countOfBigBorders;
    }
}