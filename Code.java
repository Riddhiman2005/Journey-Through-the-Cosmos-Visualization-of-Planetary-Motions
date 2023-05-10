
import processing.core.*;

public class EarthRevolution extends PApplet {

  float radius;
  float angle = 0;
  PImage bg;
  
  public void settings() {
    size(800, 800, P3D);
  }
  
  public void setup() {
    bg = loadImage("space.jpg"); // Load the space background image
    radius = height * 0.4f; // Set the radius of the orbit
    stroke(255);
    strokeWeight(2);
  }

  public void draw() {
    background(bg);
    translate(width/2, height/2);
    rotateY(angle);
    pointLight(255, 255, 255, 0, 0, 0); // Add a point light to make the Earth visible
    fill(0, 0, 255);
    noStroke();
    sphere(10); // Draw the Earth
    drawOrbit();
    angle += 0.01;
  }

  void drawOrbit() {
    noFill();
    stroke(255, 100);
    ellipse(0, 0, radius*2, radius*2);
  }

  public static void main(String[] args) {
    PApplet.main("EarthRevolution");
  }
}
