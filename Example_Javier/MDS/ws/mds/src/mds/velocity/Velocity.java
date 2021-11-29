
package mds.velocity;

import mds.common.*;
public class Velocity implements mds.common.IVelocity {
  /**
   * The state for which velocities and positions are calculated.
   * This value is initialized by the constructor.
   */
  protected mds.common.State s;

  /**
   * The object that will be used to do the calculus of accelerations,
   * It is initialized by the constructor.
   */
  protected mds.common.IForce f;

  /**
   * This static method returns a Velocity object that implements the interface IVelocity
   * 
   * @param s the state for whose particles the velocities and positions will be 
   * calculated when requested
   * @param f the force calculation object that will assign accelerations
   * @return an object of a class that implements the interface IVelocity
   */
  public static mds.common.IVelocity createVelocity(mds.common.State s, mds.common.IForce f)
  {
    
    		  return new Velocity(s, f);
  }

  /**
   * This constructor receives the state for which the Velocity object
   * will be created and the force object that calculates the acceleration
   * of all particles.
   * 
   * @param s the state for whose particles the velocities and positions 
   * will be calculated when requested
   * @param f the force calculation object that will assign accelerations
   */
  public Velocity(mds.common.State s, mds.common.IForce f) {
    	this.s = s;
    	this.f = f;
  }

  /**
   * This operation calculates the positions and velocities for the given 
   * state and force objects. It returns the largest of the displacements of the 
   * particles of the system since the last calculation of the neighbours lists.
   * It must update the kinetic energy of the current state.
   * 
   * @return the largest of the displacements of the particles since the last time the vicinity was calculated. 
   */
  public double calcVelocity() {
    return 0;
  }

}
