using System;
using System.IO;
using UnityEngine;

public class FileWatcher : MonoBehaviour
{
    private FileSystemWatcher watcher;
    public string filePath;

    // Add a public variable to hold the reference to the drone's Transform.
    public Transform droneTransform;

    void Start()
    {
        watcher = new FileSystemWatcher();
        watcher.Path = Path.GetDirectoryName(filePath);
        watcher.Filter = Path.GetFileName(filePath);
        watcher.NotifyFilter = NotifyFilters.LastWrite;
        watcher.Changed += OnChanged;
        watcher.EnableRaisingEvents = true;
    }

    private void OnChanged(object source, FileSystemEventArgs e)
    {
        if (e.FullPath == filePath)
        {
            Debug.Log("File changed: " + e.FullPath);

            // Read the updated file
            string[] lines = File.ReadAllLines(filePath);

            // Check if there are at least 3 lines for X,Y,Z coordinates.
            if (lines.Length >= 3)
            {
                // Try to parse the lines into float values.
                if (float.TryParse(lines[0], out float targetX) &&
                    float.TryParse(lines[1], out float targetY) &&
                    float.TryParse(lines[2], out float targetZ))
                {
                    Vector3 newTargetPos = new Vector3(targetX, targetY, targetZ);

                    // Set the position of your drone directly.
                    droneTransform.position = newTargetPos;
                }
                else
                {
                    Debug.LogError("Could not parse file content to coordinates.");
                }
            }
            else
            {
                Debug.LogError("Not enough data in file to determine coordinates.");
            }


        }
    }

    void OnApplicationQuit()
    {
        if (watcher != null)
        {
            watcher.Dispose();
        }
    }
}
