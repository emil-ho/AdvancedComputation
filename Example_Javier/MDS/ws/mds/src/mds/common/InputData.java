
package mds.common;

import java.util.*;
import java.io.*;
/**
 * Container of all the information needed to perform the simulation. It reads the data 
 * from the text file passed as parameter.
 */
public class InputData {
  /**
   * 
   * Unit System used for all the magnitudes(REDUCED, IS or CGS).
   * 
   */
  public final IInit.UnitSystems unitSystem;

  /**
   * Time step used for the simulation.
   */
  public final double timeStep;

  /**
   * Total time the simulation will run.
   */
  public final double totalTime;

  /**
   * Simulation identifier.
   */
  public final String nickname;

  /**
   * Parameter with length dimension of the biparametric potential.
   * Sigma for the Lennard-Jones potential.
   */
  public final double lengthParam;

  /**
   * Energy dimension parameter of the biparametric potential.
   * Epsilon for the Lennard-Jones potential.
   */
  public final double energyParam;

  /**
   * Density of the bulk of atoms.
   */
  public final double density;

  /**
   * Mass of the simulated atoms.
   */
  public final double mass;

  /**
   * Atomic number of the simulated atom.
   */
  public final int atomicNumber;

  /**
   * Initial temperature.
   */
  public final double temperature;

  /**
   * Size of the system (expressed in sigma units). This is the total length of the supercell in any of the three dimensions.
   */
  public final double systemSize;

  /**
   * Number of cells in every direction of the supercell.
   */
  private int nCells = 0;

  /**
   * Cutoff radius considered for the Lennard-Jones potential (in sigma units).
   */
  public final double cutoffRadius;

  /**
   * Safety distance for the neighbour list recalculation (in sigma units).
   */
  public final double skinRadius;

  /**
   * 
   * Type of potential used in the simulation.
   * 
   */
  public final IForce.TypeOfPotential potential;

  /**
   * 
   * Type of the initial lattice.
   * 
   */
  public final IInit.TypeOfCellLattice initialLattice;

  /**
   * Noose-Hover thermostat parameter.
   */
  public final double NoseHooverThermostatParam;

  /**
   * 
   * Algorithm that will be used to compute the evolution on time of positions and velocities.
   * 
   */
  public final IVelocity.VelocityComputingAlgorithm computingAlgorithm;

  /**
   * Fraction of the steps of the simulation that will be taken in the animation movie
   */
  public final double simulationFraction;

  /**
   * Fraction of the simulation from which the fraction of the simulation that will 
   * be taken for the animation movie will start tobe be recorded
   */
  public final double startingFraction;

  /**
   * Full path of the folder where all files will be generated.
   */
  public final String outputFolder;

  /**
   * Number of segments in the X axis used for the various histograms 
   * plotted as results of the simulation. This number is also used as the 
   * number of values of distance used to generate the image of the potential. 
   */
  public final int histogramResolution;

  /**
   * This is the length of the edge of a micro cubic cell in reduced units. 
   * It is calculated as the size of the lattice divided by the number of 
   * cells in any of the three dimensions (the lattice is a cube). 
   * This value will be different for FCC and BCC lattice types.
   */
  public final double cellSize;

  /**
   * This is the integer number of micro cubic cells to observe in the movie
   * taken for each axis. The particles to observe will be those 
   * that fit in the cube formed by that number of cells taken in each 
   * of three coordinated axis and centered in the system. 
   * If this takes the value 2 for example it indicates that particles 
   * in the 8 cells that touch the center of the system will be recorded.
   */
  public final int cellsInMoviePerAxis;

  /**
   * List of data collected from each step of the simulation. It has the
   * values of the kinetic and potential energies at each step of the simulation.
   */
  public List<EnergyLog> energyLog;

  /**
   * List of states that will be used for creating the animation. Only 
   * a fraction of the steps is stored in this list, and only a fraction of the lattice is 
   * stored in the set of particles
   */
  public List<State> movie;

  /**
   * 
   * This reference serve to provide the InitialVelocityDistribution graph to the output module.
   * 
   */
  public Graph InitialVelocityDistribution;

  /**
   * Constructor of the object. Reads the file whose full path is given as input 
   * argument, initializes the attributes and writes the log file.
   * 
   * @param simulationData a string with the full path of the file that gives values to all the
   * attributes of the object.
   * @throws ExperimentNotCreated 
   */
  public InputData(String simulationData) throws InputData.ExperimentNotCreated {
		//creates the experiment with the data in the text file
		//Use "." as decimal separator
		Locale.setDefault(Locale.ENGLISH);

		//TODO: 


		/*g80: values to consider later */
		unitSystem           =   IInit.UnitSystems.REDUCED;
		timeStep             =   1.0E-15;
		totalTime            =   1.0E-13;
		nickname             =   "SimTest";
		lengthParam          =   0.341E-9;
		energyParam          =   119.8;
		density              =   0.83684894378368910508054582719758;
		mass                 =   1.0;
		atomicNumber         =   1;
		temperature          =   0.72871452420701168614357262103506;
		systemSize           =   6.0;
		cutoffRadius         =   2.5;
		skinRadius           =   2.7;
		potential            =   IForce.TypeOfPotential.LENNARDJONES;
		initialLattice       =   IInit.TypeOfCellLattice.FCC;
		NoseHooverThermostatParam = 0.0; 
		computingAlgorithm   =   IVelocity.VelocityComputingAlgorithm.VERLET; 
		simulationFraction   =   0.02;
		startingFraction     =   0.5;
		outputFolder         =   "./output/"; 
		histogramResolution  =   100;
		cellSize             =   Math.pow(4/density,1/3);
		cellsInMoviePerAxis  =   2;
		/*    */
  }

  /**
   * Returns the value of the nCells attribute, which is calculated from the 
   * systemSize, and the density of the material.
   * 
   * @return the value of the nCells attribute.
   */
  public int getNCells() {
    return this.nCells;
  }

  /**
   * Sets the initial value of the nCells attribute. This must be loaded 
   * during the initialization of the experiment, for this reason it must  
   * be invoked with a value different than zero only once. Successive invocations 
   * will not change the first  non-zero loaded value.
   * 
   * @return true if the call has successfully initialized the attribute, false 
   * if the call has not changed the previous value sice there was already a 
   * loaded value.
   */
  public boolean setNCellsInitialValue(int nCells) {
	    if (nCells!=0) {
	    this.nCells = nCells;
	    return true;
	    }
	    return false;
  }

  /**
   * Observer method to get the lengthFactor of the conversion.
   * @return
   */
  public double factorPositions() {
		return this.lengthParam;
  }

  /**
   * Observer method to get the energyFactor of the conversion.
   * @return
   */
  public double factorEnergy() {
		return this.energyParam;
  }

  /**
   * Observer method to get the massFactor of the conversion.
   * @return
   */
  public double factorMass() {
		return this.mass;
  }

  /**
   * Observer method to get the massFactor of the conversion. 
   * @return
   */
  public double factorVelocity() {
		return Math.sqrt(this.energyParam/this.mass);
  }

  @SuppressWarnings("serial")
  public class ExperimentNotCreated extends Exception {
  }

  /**
   * Name of the text file containing the needed parameters of the kinds of 
   * particles to use for the various potentials supported (Lennard-Jones, etc).
   */
  private final String LJParameters = "LJParameters.txt";

  /**
   * 
   * This reference serve to provide the potential graph to the output module.
   * 
   */
  public Graph potentialGraph;

  /**
   * 
   * This reference serve to provide the PairDistributionFunction graph to the output module.
   * 
   */
  public Graph PairDistributionFunctionGraph;

}
