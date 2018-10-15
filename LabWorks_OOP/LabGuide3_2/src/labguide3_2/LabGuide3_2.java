
package labguide3_2;

public class LabGuide3_2 {

    public static void main(String[] args) {
        
        BookClass b1 = new BookClass();
        BookClass b2 = new BookClass("The Java Tutorial");
        BookClass b3 = new BookClass("Accounting Principles",2005, 135.8);
        BookClass b4 = new BookClass("Algorithms in C", 2008, 45.5);
        
        
        b1.display();
        b2.display();
        b3.display();
        b4.display();
        
    }
    
}
