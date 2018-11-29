import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    private static Map<Integer, List<Integer>> hirerarhy = new HashMap<Integer, List<Integer>>();

    public static void main(String args[]) {
        String inputString = "NNYNNNYNNNNNNYYN";
        int countOfEmployee = (int) Math.sqrt(inputString.length());
        createHirerarhy(countOfEmployee, inputString);

        int maxSum = 0;
        for (Integer employee : hirerarhy.keySet()) {
            int employeeSalary = getSalary(employee);
            System.out.println("E:" + employee + " has salary: " + employeeSalary);
            maxSum += employeeSalary;
        }
        System.out.println("\nTotal salary: " + maxSum);
    }

    private static void createHirerarhy(int countOfEmployee, String inputString) {
        for (int i = 0; i < countOfEmployee; i++) {
            hirerarhy.put(i, new ArrayList<Integer>());
            for (int j = 0; j < countOfEmployee; j++) {
                int index = i * countOfEmployee + j;
                char letter = inputString.charAt(index);
                if (letter == 'Y') {
                    hirerarhy.get(i).add(j);
                    System.out.println("E:" + i + " manager for " + j);
                }
            }
        }
    }

    private static int getSalary(int employee) {
        if (hirerarhy.get(employee).isEmpty()) {
            return 1;
        }
        int sum = 0;
        for (Integer worker : hirerarhy.get(employee)) {
            sum += getSalary(worker);
        }
        return sum;
    }
}
