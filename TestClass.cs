using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace NeuralNetwork
{
    public class Dendrite
    {
        private double wt;
        public double Weight
        {
            get { return wt; }
            set { wt = value; }
        }

        //Provide a constructor for the class.
        //It is always better to provide a constructor instead of using
        //the compiler provided constructor
        public Dendrite()
        {
            wt = getRandom(0.00000001, 1.0);
        }

        private double getRandom(double MinValue, double MaxValue)
        {
            Random random = new Random();
            return random.Next(1) * (MaxValue - MinValue) + MinValue;
        }

    }

    class Neuron
    {
        private List<Dendrite> dendrites;
        private double bias, delta, _value;

        public double Bias
        {
            get
            { return bias; }
            set
            { bias = value; }
        }
        public double Delta
        {
            get
            { return delta; }
            set
            { delta = value; }
        }
        public double Value
        {
            get
            { return _value; }
            set
            { _value = value; }
        }

        public void AddDendrites(int nDendrites)
        {
            //Dendrite d;
            for (int i = 0; i < nDendrites; i++)
            {
                //d = new Dendrite();
                dendrites.Add(new Dendrite());
            }
        }

        public int nDendrites()
        {
            return dendrites.Count;
        }

        public Dendrite getDendrite(int index)
        {
            return dendrites[index];
        }

        public Neuron()
        {
            Random random = new Random();
            bias = random.Next(1);
            dendrites = new List<Dendrite>();
        }

    }

    class Layer
    {
        private List<Neuron> neurons;

        public void Clear()
        {
            neurons.Clear();
        }
        public void Initialize(int nNeurons)
        {
            int i;
            for (i = 0; i < nNeurons; i++)
            {
                neurons.Add(new Neuron());
            }
        }

        public Neuron getNeuron(int index)
        {
            return neurons[index];
        }
        public void setNeuron(int index, ref Neuron neuron)
        {
            neurons[index] = neuron;
        }
        public void setNeuron(int index, Double value)
        {
            Neuron n = new Neuron();
            n.Value = value;
            neurons[index] = n;
        }

        public void AddDendritesToEachNeuron(int nDendrites)
        {
            int i;
            for (i = 0; i < neurons.Count; i++)
            {
                neurons[i].AddDendrites(nDendrites);
            }
        }

        public int nNeurons()
        {
            return neurons.Count;
        }



        /// <summary>
        /// Constructor of the class
        /// </summary>
        public Layer()
        {
            neurons = new List<Neuron>();
        }
    }
}
