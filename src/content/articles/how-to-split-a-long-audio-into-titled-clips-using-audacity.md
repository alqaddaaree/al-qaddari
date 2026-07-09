---
title: "How to Split a Long Audio into Titled Clips Using Audacity"
date: 2024-01-01
description: |
  A small technical benefit for anyone working with long audio recordings. I was preparing a tape of al-Albānī رحمه الله and needed to split it into smaller clips. The normal way would be painful: Open ...
tags: ['audio']
source: raqmanat
language: ar
---

A small technical benefit for anyone working with long audio recordings.

I was preparing a tape of al-Albānī رحمه الله and needed to split it into smaller clips. 

The normal way would be painful:

Open the audio.  
Select the first part.  
Export it.  
Go back.  
Select the next part.  
Export it.  
Repeat.  
Make mistakes.  
Lose patience.  
Question your life choices. 

But Audacity can do this in a much cleaner way.

You can give Audacity a list of timestamps, import them as labels, and then export all the sections automatically. 

For example, I had a tape with sections like this:
    
    
    0:00 مقدمة المترجم ، وتاريخ مولد الشيخ الألباني
    3:48 هل كان مسقط رأسك في دمشق أم في ألبانيا
    4:20 هل كان دخولكم دمشق الشام مع الوالد نتيجة اضطهاد
    6:10 كم كان لك من العمر في ذلك الوقت حين هاجر والدك إلى الشام

Each timestamp is where a new audio section begins.

So the first section starts at **0:00** and ends at **3:48**.  
The second starts at **3:48** and ends at **4:20**.  
The third starts at **4:20** and ends at **6:10**. 

Audacity needs these labels in this format:
    
    
    START    END    TITLE

So the same list becomes:
    
    
    0.000000	228.000000	مقدمة المترجم ، وتاريخ مولد الشيخ الألباني
    228.000000	260.000000	هل كان مسقط رأسك في دمشق أم في ألبانيا
    260.000000	370.000000	هل كان دخولكم دمشق الشام مع الوالد نتيجة اضطهاد
    370.000000	701.000000	كم كان لك من العمر في ذلك الوقت حين هاجر والدك إلى الشام

Notice that the times are written in seconds.

  * **3:48** becomes **228** seconds.
  * **4:20** becomes **260** seconds.
  * **6:10** becomes **370** seconds.
  * **11:41** becomes **701** seconds.



Then you save this as a plain text file, for example:
    
    
    albani-labels.txt

After that, open the audio in Audacity.

Then go to:
    
    
    File → Import → Labels

Choose the text file.

Audacity will add the labels to the audio.

Then go to:
    
    
    File → Export Audio

Choose:
    
    
    Multiple Files

Then choose:
    
    
    Split files based on Labels

Now Audacity exports each section as its own audio file, already titled from the labels. 

This is very useful for people preparing:

  * lectures,
  * translated clips,
  * question-and-answer tapes,
  * lesson archives,
  * Telegram audio posts,
  * or anything long that needs to be cut into smaller parts.



**Small warning:**

The label file must be plain text, and the columns should be separated by real tabs: 
    
    
    start time    end time    title

If Audacity says the labels could not be read, the problem is usually the formatting. 

Use seconds, use tabs, and save it as `.txt`. 

Very simple once it works.

A long tape becomes organized clips in one export. 

Tiny tool, huge relief. 

اللهم لك الحمد ولك الشكر. 
