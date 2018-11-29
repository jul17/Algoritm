import java.util.List;
import java.util.Scanner;

public class PainterManager {
    int time;
    int countOfPainters;

    public PainterManager() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter count of Painters: ");
        countOfPainters = scan.nextInt();
        System.out.println("Enter Time for painters: ");
        time = scan.nextInt();
    }




    public PainterManager(int time, int countOfPainters) {
        this.time = time;
        this.countOfPainters = countOfPainters;
    }

    public int getMaxTime(List<Integer> countOfBigBorders) {
        int max = 0;
        for (Integer value : countOfBigBorders) {
            if (value > max) {
                max = value;
            }
        }
        return max * time;
    }

    public List<Integer> getBigbordersForPainters(List<Integer> countOfBigBorders) {
        while (this.countOfPainters != countOfBigBorders.size()) {
            int startIndex = 0;
            int minSum = countOfBigBorders.get(0) + countOfBigBorders.get(1);
            for (int i = 0; i < countOfBigBorders.size() - 1; i++) {
                if (minSum > countOfBigBorders.get(i) + countOfBigBorders.get(i + 1)) {
                    minSum = countOfBigBorders.get(i) + countOfBigBorders.get(i + 1);
                    startIndex = i;
                }
            }
            countOfBigBorders.set(startIndex, minSum);
            countOfBigBorders.remove(startIndex + 1);
            System.out.println(minSum);
        }

        return countOfBigBorders;
    }

    public int getCountOfPainters() {
        return countOfPainters;
    }


}