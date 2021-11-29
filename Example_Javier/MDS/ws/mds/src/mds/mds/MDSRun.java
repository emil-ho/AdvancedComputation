
package mds.mds;

import mds.common.*;
import mds.init.*;
import mds.output.*;
import mds.force.*;
import mds.velocity.*;
import mds.neighbours.*;
import java.util.*;
/**
 * Basic services to run the simulation
 */
public class MDSRun implements mds.common.IMDS {
  /**
   * This class has the states in which the simulation can be
   */
  enum RunningState {
    UNINTERRUPTIBLE,/**
     * This is the state used to indicate non concurrent simulations
     * that will run to completion and hence are not managed.
     */

    READY,/**
     * Indicates that the simulation has not been launched yet.
     */

    PAUSE,/**
     * This state indicates that the simulation should be stopped and stay stopped.
     */

    PAUSED,/**
     * This state indicates that the simulation has been stopped and stay stopped.
     */

    RUNNING,/**
     * This is the normal state when the simulation runs in a separate thread
     */

    DONE,/**
     * This is the state that indicates that the simulation has finished and is waiting 
     * for its results to be recalled. This is necessary when  the simulation runs in 
     * a separate thread
     */
;
  }

  /**
   * Internal attribute used to manage a running simulation
   */
  private MDSRun.RunningState runningState = RunningState.READY;

  /**
   * This is the current step of the simulation
   */
  private int step;

  /**
   * This is the total number of steps of the simulation
   */
  private int nSteps;

  /**
   * This is the handler for the concurrent thread in which the
   * simulation will run if requested.
   */
  private Thread simulationThread;

  /**
   * The experiment to run in the concurrent thread.
   */
  private mds.common.InputData concurrentExperiment;

  /**
   * The resultFiles object to store and return after a concurrent simulation.
   */
  private mds.common.ResultsFiles concurrentResults;

  /**
   * This static method returns a simulator object that implements the interface IMDS 
   * 
   * @return an object that implements the interface IMDS
   */
  public static mds.common.IMDS createSimulator()
  {
    	return new MDSRun();
  }

  /**
   * Default constructor
   */
  public MDSRun() {
  }

  /**
   * It runs a simulation of the given experiment up to completion and produces 
   * the output results. 
   * 
   * @param experiment is the experiment object with the data needed to configure and 
   * run the simulation
   * @return returns the ResultsFile object with the names of all the requested 
   * resulting data files generated. If any of those files could not 
   * be generated the corresponding string would be a null reference. It returns null
   * if the simulation is in an inadequate state to be started in an uninterruptible way.
   */
  public mds.common.ResultsFiles simulate(mds.common.InputData experiment) {
    	if (runningState != RunningState.READY) return null;
    	
    	//this indicates that the simulation will not be able to be interrupted
    	runningState = RunningState.UNINTERRUPTIBLE;
    	
    	//run it up to completion
        ResultsFiles results = simulation (experiment);
    	
        //reset the state to enable it to run again
        runningState = RunningState.READY;
        
        return results;
  }

  /**
   * Starts a concurrent simulation for the experiment given as parameter.
   * When it returns, the simulation has been already initiated
   * and the steps are advancing.
   * 
   * @param experiment is the experiment object with the data needed to 
   * configure and run the simulation.
   */
  public boolean startSimulation(mds.common.InputData experiment) {
    if (runningState != RunningState.READY) return false;
    
    //this indicates that the simulation is running concurrently
    runningState = RunningState.RUNNING;
        
    //store the experiment in the attribute
    concurrentExperiment = experiment;
    
    //create the thread to run it
    simulationThread = new Thread(this);
    
    //start the run() operation
    simulationThread.start();
    
    //returns control to the caller
    return true;
  }

  /**
   * Indicates the fraction of the simulation at which the simulator is currently running.
   * 
   * @retuns a double value from 0 to 1 indicating the fraction of the simulation 
   * already performed. 0 means it has not started, 1 means it has already finished.
   */
  public double currentSimulationFraction() {
    	return ( (double) step ) / ( (double) nSteps );
  }

  /**
   * Stops the advance of the simulation if it is running. 
   * 
   * @return It returns true if it was succesfully paused, and 
   * false in case the simulation was already paused or not 
   * started to run concurrently.
   */
  public boolean pauseSimulation() {
    		if (runningState != RunningState.RUNNING) return false;
    
    		//signal the simulation thread to stop executing 
    		//the simulation and simply wait
    		runningState = RunningState.PAUSE;
    
    		//wait until the simulation is effectively paused
    		while(runningState != RunningState.PAUSED) {
    			try{ Thread.sleep(500);
    			}catch (InterruptedException e){
    				//if an interrupt signal is received there is not guarantee that the simulation could be stopped
    				return false;
    			}
    		}
    		return true;
    
    	  
  }

  /**
   * Continues a simulation previously paused.
   * 
   * @return It returns true if the simulation was succesfully continued, and 
   * false in case the simulation was already running or not 
   * started to run concurrently.
   */
  public boolean continueSimulation() {
    		if (runningState != RunningState.PAUSED) return false;
    
    		int currentStep = step;
    
    		//signal the simulation thread to continue executing 
    		//the simulation
    		runningState = RunningState.RUNNING;
    
    		//wait until the simulation is effectively running
    		while(step == currentStep) {
    			try{ Thread.sleep(500);
    			}catch (InterruptedException e){
    				//if an interrupt signal is received there is not guarantee that the simulation could be put to run again
    				return false;
    			}
    		}
    		return true;
  }

  /**
   * It saves the current status on disk so that in case of need the simulation 
   * can be restarted from the saved point.  
   * If the simulation is running it pauses the advance of the simulation after the 
   * current step is done before saving, and continues running again. 
   * 
   * @return a String with the name of the file holding the status of the simulation. 
   * A not initialized or already finished simulation returns a null String
   */
  public String saveSimulation() {
	return null;
  }

  /**
   * Continues a simulation previously stored to disk. If the simulation is currently running
   * it is stopped,  the experiment is dismissed,  and it gets started from the saved file status.
   * 
   * @param savedSimulationFile a string indicating the full path of a file holding the status of a 
   * previously saved simulation.
   */
  public void continueSavedSimulation(String savedSimFile) throws mds.common.ILongSimulationManager.FileNotFound, mds.common.ILongSimulationManager.FileCorrupted {
  }

  /**
   * *
   *  * Returns the output results if the simulation has finished or a null pointer if it has not
   *  *
   *  * @return returns the ResultsFile object with the names of all the requested 
   *  * resulting data files generated. If any of those files could not 
   *  * be generated the corresponding string would be a null reference.
   *  
   */
  public mds.common.ResultsFiles getSimulationResults() {
    if (runningState != RunningState.DONE) return null;
    
    return concurrentResults;
  }

  /**
   * This function is used to execute the simulation concurrently
   */
  public void run() {
    	  
    	  //run it concurrently
          concurrentResults = simulation (concurrentExperiment);
      	
          //set the state to enable the caller to get results back
          runningState = RunningState.DONE;
  }

  /**
   * This operation runs a simulation of the given experiment up to completion and produces 
   * the output results. If it is running in a concurrent thread it can be
   * paused and continued.
   * 
   * @param experiment is the experiment object with the data needed to configure and 
   * run the simulation
   * @return returns the ResultsFile object with the names of all the requested 
   * resulting images and data files generated. If any of those files could not 
   * be generated the corresponding string would be a null reference.
   */
  private mds.common.ResultsFiles simulation(mds.common.InputData experiment) {
    
    	  /* Calculate_nSteps&MovieSteps */
    
    	  //Calculate the number of steps
    	  nSteps = (int) Math.round(experiment.totalTime / experiment.timeStep);
    	  //calculate the step to start taken samples for the movie
    	  int startMovieStep = (int) (experiment.startingFraction*(double)nSteps);
    	  //calculate the final step to take samples
    	  int endMovieStep = startMovieStep + (int) (experiment.simulationFraction*(double)nSteps);
    	  endMovieStep=(endMovieStep>nSteps)?nSteps:endMovieStep;
    
    	  //prepare the list to take the log of the system (energies)
    	  experiment.energyLog = new ArrayList<EnergyLog>(nSteps);
    	  //prepare the list to take the movie samples
    	  experiment.movie = new ArrayList<State>(endMovieStep-startMovieStep+1);
    
    	  /* Initial setup for the simulation  */
    
    	  //Create the initialization object 
    	  IInit init = mds.init.Init.createInit();
    	  //Invoke doInit() to get the initial state
    	  State s= init.doInit(experiment);
    	  experiment.InitialVelocityDistribution = init.getInitialVelocityDistribution();
    
    	  //Create the neighbours list management object
    	  INeighbours neighbours = mds.neighbours.Neighbours.createNeighbours(s);
    
    	  //Set the initial neighbours lists
    	  neighbours.calcVecinity(experiment.skinRadius+1);
    
    	  //Create the force calculation object
    	  IForce force = mds.force.Force.createForce(s);
    
    	  //Create the Velocity calculation object
    	  IVelocity velocity = mds.velocity.Velocity.createVelocity(s, force);
    
    	  //calculate the initial accelerations 
    	  //and take the potential energy it in the system log object
    	  s.energy.u = force.calcForce();
    
    	  //store the first state log in the experiment log list
    	  experiment.energyLog.add((EnergyLog) s.energy.clone());
    
    	  //create the list of particles in the visualization scope
    	  List<Particle> sampleScope = new ArrayList<Particle>();
    
    	  //calculus of the borders of the cube of interest
    	  double safetymargin = experiment.cellSize/4;
    	  double posBorder = experiment.cellSize*experiment.cellsInMoviePerAxis/2.0 + safetymargin;
    	  double negBorder = posBorder * (-1);
    
    	  //take the particles of interest from the complete list into the sampleScope  
    	  for (Particle p: s.particles){
    		  // if its position is in the scope
    		  if ( (p.r.x > negBorder && p.r.x < posBorder) && 
    				  (p.r.y > negBorder && p.r.y < posBorder) &&
    				  (p.r.z > negBorder && p.r.z < posBorder)    ) {
    			  sampleScope.add(p);
    		  }
    	  }
    
    
    	  /* Do the simulation  */
    	  simulationLoop:
    		  for(step=0; step<nSteps; step++) {
    
    			  //We simulate a time step for the current state.
    			  //and update the vicinity if needed
    			  neighbours.calcVecinity(velocity.calcVelocity());
    
    			  //store the current state log in the experiment log list
    			  experiment.energyLog.add((EnergyLog) s.energy.clone());
    
    			  //Check if a sample for the movie needs to be taken at this step 
    			  //and, if so, take the sample
    			  if (step>=startMovieStep && step<=endMovieStep) {
    				  //get a copy of the state with the sample of particles 
    				  //that fit in the visualization scope
    				  experiment.movie.add(s.copy(sampleScope));
    			  }
    
    			  stopIfRequested:
    				  if (runningState == RunningState.PAUSE) {
    					  runningState = RunningState.PAUSED;
    					  while(runningState == RunningState.PAUSED) {
    						  try{ Thread.sleep(500);
    						  }catch (InterruptedException e){
    							  Thread.currentThread().interrupt();}
    					  }
    				  }
    		  }
    
    	  //Create the output production object
    	  IOutput out = new mds.output.Output();
    	  return out.results(experiment, new ResultsFiles(experiment.outputFolder, experiment.nickname));
  }

}
