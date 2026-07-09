---
title: "How to Run Maktaba Shamela on Linux (Fedora KDE)"
date: 2026-04-20
description: |
  This is a guide to getting Al-Maktabah Shamela running on Fedora KDE. If you’ve struggled with crashes, weird symbols, or the app simply refusing to open, this is for you.
tags: ['general']
source: raqmanat
language: ar
---

This is a guide to getting **Al-****Maktabah Shamela** running on **Fedora KDE**. If you’ve struggled with crashes, weird symbols, or the app simply refusing to open, this is for you.

* * *

  


Running legendary Arabic software like Maktaba Shamela on Linux used to be a nightmare because it relies on very old Windows technologies (Visual Basic 6 and legacy Python). But with a tool called **Bottles** , we can build a perfect "home" for it.

###  

### 📋 Phase 1: Pre-Flight Checklist

Before we touch any software, you need three things:

  1. **The Shamela Installer:** Your `.exe` or `.zip` file from the official site.

  2. **The Secret DLLs:** Go to a DLL archive site (like [dll-files.com](https://www.dll-files.com/)) and download:

     * `libcrypto-1_1.dll`

     * `libssl-1_1.dll`

     *  _(Note: If they have -64 in the name, just rename them later to exactly the above)._

  3. **An Internet Connection:** Fedora needs to download some "compatibility layers."




* * *

###  

### 📦 Phase 2: Installing the Foundation

We are going to use **Bottles** , which is the best way to run Windows apps without breaking your Linux system.

  1. Open **Discover** (the blue shopping bag icon in your KDE menu).

  2. Search for **Bottles**.

  3. Click **Install**.

  4. Once installed, open it.




* * *

###  

### 🛠 Phase 3: Building the "Bottle"

Think of a "Bottle" as a mini-Windows computer living inside your Linux.

  1. Click the **\+ (plus)** button in Bottles.

  2. **Name:** Type `Shamela`.

  3. **Environment:** Choose **Application**.

  4. Click **Create**. Wait for the blue bar to finish. This sets up the folder structure.




* * *

###  

### 💉 Phase 4: Installing Critical Dependencies

This is the step most people forget. Shamela is old school; it needs specific Windows "guts" to breathe.

  1. Click on your new **Shamela** bottle.

  2. On the left sidebar, click **Dependencies**.

  3. In the search bar, find and install these (click the download icon next to each):

     * `vb6run`: (Visual Basic 6 runtime—mandatory for Shamela).

     * `cjkfonts` or `allfonts`: (Crucial for Arabic text support so you don't see squares).

     * `vcredist2015`: (Common C++ libraries).




* * *

###  

### 📂 Phase 5: The Manual DLL "Hack"

Shamela’s search and database features use Python, which requires OpenSSL files that Wine usually misses.

  1. In Bottles, click **Browse Files** (bottom of the screen). This opens your virtual Windows drive (`drive_c`).

  2. Navigate to: `windows\``system32`.

  3. Take your downloaded `libcrypto-1_1.dll` and `libssl-1_1.dll` and **copy-paste** them here.

     * **Pro Tip:** If your files are named `libcrypto-1_1-x64.dll`, you **must** rename them to `libcrypto-1_1.dll` or the app won't "see" them.




* * *

###  

### ⚙️ Phase 6: The "Anti-Crash" Settings

Modern Linux uses high-speed graphics drivers (Vulkan) that older Windows apps hate. We need to tell the Bottle to slow down.

  1. In Bottles, go to **Settings** (left sidebar).

  2. Scroll to **Components**. Find **DXVK** and **VKD3D** —turn them both **OFF**.

  3. Scroll to **Environment Variables**. Click the **+** button.

     * **Value:** `dxgi=d`

     * Click **Add**. (This forces the app to use its own simple graphics).

  4. Scroll to **Display** and turn **Virtual Desktop** to **ON**. (This prevents the app from flickering or disappearing when you switch windows).




* * *

###  

### 🚀 Phase 7: Installation & First Launch

  1. Go back to the main **Shamela** screen in Bottles.

  2. Click **Run Executable**.

  3. Find your `ShamelaSetup.exe` and let it run. Follow the Windows-style installation wizard.

  4. **Wait!** After it's done, Bottles should automatically show **Maktaba Shamela** in the **Programs** tab.

  5. Click the **Play** icon.




* * *

###  

### ❓ FAQ: "What if...?"

**Q: Why is the text showing up as gibberish?**

**A:** Go to the **Dependencies** tab in Bottles and ensure you installed `allfonts`. Also, make sure your system's "Regional Settings" in Fedora include Arabic support.

**Q: It says "Database not found!"**

**A:** Make sure you didn't move the Shamela folder after installing it. If you have the books on an external hard drive, you need to go to **Bottles Settings > Drive Drives** and add your external drive there.

**Q: Can I update Shamela?**

**A:** Yes! Just run the new updater `.exe` using the **Run Executable** button inside the _same_ bottle.

**Q: Why Bottles instead of just installing Wine?**

**A:** Because if you mess up a setting in Bottles, you just delete the bottle and start over. If you mess up your main Wine installation, it's a headache to clean up. Bottles keeps your Fedora "clean."

* * *

 

For anyone on Fedora KDE struggling with Shamela: The trick isn't just Wine—it's disabling DXVK, overriding the `dxgi` DLL, and manually dropping OpenSSL 1.1.1 files into System32. Works like a charm!

 

This tutorial was generated by Gemini after a session of setting up Shamela on my Fedora KDE. I thought the experience could help others that use Linus and would love to use Shamela on it. 

To contact me, you can use:

  * <https://forms.gle/NnxtgtMxVMzjxTyi8>
  * <https://t.me/abuSahlInventory>


