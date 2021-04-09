using System.Collections;
using System.Collections.Generic;

namespace CarLibrary
{
    public abstract class Car
    {
        public string Maker { get; set; }
        public int Number { get; set; }
        public string Color { get; set; }

        private int EngineStatus = 1;

        public Car(){}
        
        public Car(string maker, int number, string color)
        {
            Maker = maker; Number = number; Color = color;
        }

        public abstract void Drive();

        public virtual int GetEngineStatus();

    }

    public sealed class SportsCar: Car
    {
        private new int EngineStatus = 69;
        public int MaxSpeed { get; set; }
        public SportsCar(){}
        public SportsCar(string maker, int number, string color, int maxSp)
        : base(maker, number, color)
        {
            MaxSpeed = maxSp;
        }

        public override void Drive()
        => "SportsCar is moving!";

        public override int GetEngineStatus()
        => EngineStatus;

        public override string ToString()
        => $"\nMaker: {Maker}\nNumber: {Number}\nColor: {Color}\nMaxSpeed: {MaxSpeed}";
        
    }

    public class SportsCarCollection: IEnumerable
    {
        private SportsCar[] sportsCars;
        public SportsCarCollection(int n)
        {
            sportsCars = new SportsCar[n]{};
        }

        public Enumerator GetEnumerator()
        {
            return sportsCars.GetEnumerator();
        }

    }


}