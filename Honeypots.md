# Dr honeypots :
How I stop worrying and know my ennemies.



* Use of honeypost  in digital forensics and icicent responde.


## History of honeypots

"Cuckoo's Egg" : novel on the intrusion by Lawrence Berlekley Lab? Bu CLifford Stoll.
First APT.
Honeypots as a mean to detect the level of threat.


## Definition of a HoneyPot :
It's a Trap !

* Find techniques the guy suses to discover
* Fund wher's it's interested the most in
* Don not make him find that it's in teha trap.


Trap has to be carfully made but it can bite !

Honeynet : network as a Honeypots

## Honeypot
* Everyting happeing in a honeypot is suspicious by nature
* You must monitor everytihgn in your honeypot.


## Honeypot for CERT/CSIRT

## Counter-OSINT
Honeytoken : data as a honeypot :
* Fake linkedin profile
* (hidden in HTML code
* faked leaked data on Pastebin
* Fake password hash loaded in memory to detect password stealers (mimikatz)

* Register dake domain name.
* DNS WHOIS
* Fake webcam associated with an unused IP from your range

## Critical Points
- Montiro/store/coellect data
- Allow, Forbid/restrid internet acces
- HDo you hide your honeypot or do you make it public (DNS, domain, IP) ??

### Collecting data
How can I monitor an intruder wiht priviledged access without being detected/defeated ?
### Avoid Detection
Talk at BalckHat 2015 on how to break honeypots

# Existing honeypots

## Server-side
* Dioneea (simulates vulnerabilities on a Windows)
* Honeyd : acts as eid daemon in linux. Can be attached to a port.
        Modify the TCP stack of the machitn to mimic another one.
* Honeytrap
* VoIP : atermisa
* SSH : Cowrie
* SCADA : Conpot can emulate a complete power plant !!
*
## Client-side
* Thig : simualted a vinerable browser.
If you connect wit this via the honeypot, it will tell you what the besite is tyring to fo..


## Hybird
* BiFrozt for SSH (detect SSH traffic between the attacker and the normal SSH server.)

PhoneyC


# Hands-on

Kippo : fake SSH server in python


HonerDrive :



Glastopf : dummy website that anwwers alcays by Yes.
    Embed a PHP sandwbow to emulat a code injection.




# Resources

Books :
* Proactive Detection of Security Incicendts (by ENISA)
* Know your enemy (another book)

Book of 2012 on honeypots
