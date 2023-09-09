using UnityEngine;
using UnityEngine.UI;

public class DisplayPosition : MonoBehaviour
{
    public Transform droneA; // Drone A Transform
    public Transform droneB; // Drone B Transform

    public Text textAX; // UI text for Drone A X position
    public Text textAY; // UI text for Drone A Y position
    public Text textAZ; // UI text for Drone A Z position

    public Text textBX; // UI text for Drone B X position
    public Text textBY; // UI text for Drone B Y position
    public Text textBZ; // UI text for Drone B Z position

    void Update()
    {
        if (droneA != null && droneB != null)
        {
            Vector3 posA = droneA.position;
            Vector3 posB = droneB.position;

            UpdateText(textAX, "Drone A X Position: ", posA.x);
            UpdateText(textAY, "Drone A Y Position: ", posA.y);
            UpdateText(textAZ, "Drone A Z Position: ", posA.z);

            UpdateText(textBX, "Drone B X Position: ", posB.x);
            UpdateText(textBY, "Drone B Y Position: ", posB.y);
            UpdateText(textBZ, "Drone B Z Position: ", posB.z);
        }

        void UpdateText(Text uiElement, string prefix, float value)
        {
            uiElement.text = prefix + value.ToString("F2");
        }
    }
}
