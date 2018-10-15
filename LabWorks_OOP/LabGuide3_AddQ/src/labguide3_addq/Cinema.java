
package labguide3_addq;


public class Cinema {
    public static void main(String[] args) {
        
        Director d1 = new Director();
        
        d1.setName("Evren Aykaç");
        
        d1.display();
        System.out.println(d1.getName() + d1.getInfo() + ", earns "+ d1.earnings() + "$ per film");
        
        Director d2 = new Director ("Steven Spielberg", 161, 17, "is well known with Schindler’s Listand Saving Private Ryan");
        d2.display2();
       
    }
    
}
