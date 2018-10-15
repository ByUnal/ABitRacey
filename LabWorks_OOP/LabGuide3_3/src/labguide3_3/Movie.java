
package labguide3_3;

public class Movie {
    
    String title;
    int year;
    double rating;

    public Movie(String title, int year, double rating) {
        this.title = title;
        this.year = year;
        this.rating = rating;
    }

    public Movie(String title, int year) {
        this.title = title;
        this.year = year;
    }

    public Movie(String title) {
        this.title = title;
    }

    public Movie() {
        title = null;
        year = 0;
        rating = 0.0;
    }
    
    public void display(){
        System.out.printf(title + " , " + year + " ," + rating + " points. " + "\n");
    }
    
    
    
}
