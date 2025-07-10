<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $message = $_POST["message"] ?? '';
    $escaped = escapeshellarg($message);

    // Full command with error output
    $command = "python spam_classifier.py $escaped 2>&1";
    $output = shell_exec($command);
    $output = trim($output);

    if ($output === '') {
        echo "⚠️ No output. Check if Python is installed and the script is working.";
    } else {
        echo $output;
    }
}
?>