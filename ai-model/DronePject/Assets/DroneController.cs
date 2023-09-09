using UnityEngine;
using System.IO;
using UnityEngine.UI;

public class MoveDrone : MonoBehaviour
{
    public float speed = 5.0f;
    private Vector3 targetPosition;
    private bool isMoving = false;
    public string filePath;
    public Text textX; // UI Text component for displaying the drone's X position
    public Text textY; // UI Text component for displaying the drone's Y position
    public Text textZ; // UI Text component for displaying the drone's Z position

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Return))
        {

            if (File.Exists(filePath))
            {
                string[] lines = File.ReadAllLines(filePath);
                if (lines.Length >= 3)
                {
                    if (float.TryParse(lines[0], out float targetX) &&
                        float.TryParse(lines[1], out float targetY) &&
                        float.TryParse(lines[2], out float targetZ))
                    {
                        targetPosition = new Vector3(targetX, targetY, targetZ);
                        isMoving = true;

                        // Update the text components with the new positions
                        textX.text = $"Target X: {targetX}";
                        textY.text = $"Target Y: {targetY}";
                        textZ.text = $"Target Z: {targetZ}";
                    }
                }
            }
        }

        if (isMoving)
        {
            transform.position = Vector3.MoveTowards(transform.position, targetPosition, speed * Time.deltaTime);

            if (transform.position == targetPosition)
            {
                isMoving = false;
            }
        }
    }
}
