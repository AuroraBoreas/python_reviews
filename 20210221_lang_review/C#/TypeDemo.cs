using System;

namespace MyTypes
{
    public enum Colors
    {
        red,
        green,
        blue,
        yellow,
        purple,
        orange,
    }

    public struct Point
    {
        public int X { get; set; }
        public int Y { get; set; }

        public Point(int x, int y)
        {
            X = x; Y = y;
        }

        public override string ToString()
        {
            return $"[{X}, {Y}]";
        }           
    }

    public class Person
    {
        // data fields
        private string m_name;
        private string m_sex;
        private int m_age;

        // ctors
        public Person(){}   // default ctor
        public Person(string name)
        : this(name, "", 0){}   // delegate ctor
        public Person(string sex)
        : this("", sex, 0){}
        public Person(int age)
        : this("", "", age){}
        public Person(string name, string sex, int age) // "master" ctor
        {
            m_name = name;
            m_sex = sex;
            m_age = age;
        }

        // getter
        public string Name()
        { return m_name; }
        public string Sex()
        { return m_sex; }
        public int Age()
        { return m_age; }

        // setter
        public void Name(string val) => m_name = val;
        public void Sex(string val) => m_sex = val;
        public void Age(int val) => m_age = val;

        // override
        public override string ToString()
        {
            return string.Format("\nName: {0}\nSex: {1}\nAge: {2}", m_name, m_sex, m_age);
        }
    }

    public class CarV0
    {
        public string Maker { get; set; }
        public int MaxSpeed { get; set; }
        public int CurrentSpeed { get; set; }
        public string Color { get; set; }
        private bool IsEngineDead = false;

        public CarV0(){}
        public CarV0(string maker, int maxSp, int curSp, string color)
        {
            Maker = maker;
            MaxSpeed = maxSp;
            CurrentSpeed = curSp;
            Color = color;
        }

        public override string ToString()
        => $"\nMaker: {Maker}\nMaxSpeed: {MaxSpeed}\nCurrentSpeed: {CurrentSpeed}\nColor: {Color}";

        // delegate
        public delegate void EngineStatus(string info);
        private EngineStatus EngineEvent;
        // registration and unregistration
        public void RegistrationEngineEvent(EngineStatus e)
        {
            EngineEvent += e;
        }
        public void UnregistrationEngineEvent(EngineStatus e)
        {
            EngineEvent -= e;
        }

        public void Acceleration(int delta)
        {
            CurrentSpeed += delta;
            if(IsEngineDead)
            {
                if(EngineEvent != null)
                    EngineEvent("Engine is dead");
                else
                    throw new Exception("EngineEvent is null");
            }
            else
            {
                if(MaxSpeed > CurrentSpeed && EngineEvent != null)
                {
                    IsEngineDead = true;
                    EngineEvent("Engine is dead");
                }
                else if(10 >= Math.Abs(MaxSpeed - CurrentSpeed) && EngineEvent != null)
                {
                    EngineEvent("Be careful! Engine is dangerous!");
                }
                else
                {
                    if(EngineEvent != null)
                        EngineEvent("faster is better");
                }
            }
        }
    }

    public class CarEngineEventArgs
    {
        public string Info { get; }
        public CarEngineEventArgs(string info)
        {
            Info = info;
        }
    }

    public class CarV1
    {
        public string Maker { get; set; }
        public int MaxSpeed { get; set; }
        public int CurrentSpeed { get; set; }
        public string Color { get; set; }
        private bool IsEngineDead = false;

        public CarV1(){}
        public CarV1(string maker, int maxSp, int curSp, string color)
        {
            Maker = maker;
            MaxSpeed = maxSp;
            CurrentSpeed = curSp;
            Color = color;
        }

        public override string ToString()
        => $"\nMaker: {Maker}\nMaxSpeed: {MaxSpeed}\nCurrentSpeed: {CurrentSpeed}\nColor: {Color}";

        // delegate
        public delegate void EngineStatus(object sender, CarEngineEventArgs e);
        // event
        public event EventHandler<CarEngineEventArgs> CarEngineEventHanlder;
        
        public void Acceleration(int delta)
        {
            CurrentSpeed += delta;
            if(IsEngineDead)
            {
                CarEngineEventHanlder?.Invoke(this, new CarEngineEventArgs("Engine is dead"));
            }
            else
            {
                if(MaxSpeed > CurrentSpeed)
                {
                    IsEngineDead = true;
                    CarEngineEventHanlder?.Invoke(this, new CarEngineEventArgs("Engine is dead"));
                }
                else if(10 >= Math.Abs(MaxSpeed - CurrentSpeed))
                {
                    CarEngineEventHanlder?.Invoke(this, new CarEngineEventArgs("Be careful! Engine is dangerous!"));
                }
                else
                {
                    CarEngineEventHanlder?.Invoke(this, new CarEngineEventArgs("faster is better"));
                }
            }
        }
    }
}