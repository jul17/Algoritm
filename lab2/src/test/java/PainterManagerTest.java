import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class PainterManagerTest {



    @org.junit.Test
    public void getMaxTime() {
        PainterManager painterManager = new PainterManager(10,3);
        List<Integer> countOfBigBorders = new ArrayList<Integer>();
        countOfBigBorders.add(5);
        countOfBigBorders.add(10);
        countOfBigBorders.add(15);

        int maxTime = painterManager.getMaxTime(countOfBigBorders);
        assertEquals(150, maxTime);
    }

    @org.junit.Test
    public void getBigbordersForPainters() {
        PainterManager painterManager = new PainterManager(10,2);
        List<Integer> countOfBigBorders = new ArrayList<Integer>();
        countOfBigBorders.add(5);
        countOfBigBorders.add(10);
        countOfBigBorders.add(15);

        countOfBigBorders = painterManager.getBigbordersForPainters(countOfBigBorders);
        assertEquals(2,countOfBigBorders.size());
        int maxTime = painterManager.getMaxTime(countOfBigBorders);
        assertEquals(150, maxTime);

    }

    @org.junit.Test
    public void getCountOfPainters() {
        PainterManager painterManager = new PainterManager(10,5);
        assertEquals(5,painterManager.getCountOfPainters());
    }
}