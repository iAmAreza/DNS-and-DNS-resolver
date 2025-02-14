# DNS and DNS resolver

The **Domain Name System (DNS)** is a hierarchical system that translates **human-readable domain names** (e.g., google.com) into **machine-readable IP addresses** (e.g., 142.250.190.78). It acts as the **internet’s phonebook**, enabling users to access websites without remembering numerical IP addresses.

For example ,  When we type [**www.wikipedia.org**](http://www.wikipedia.org/) into our browser, we are actually asking a **DNS server**, which acts as an intermediary between us and the **Wikipedia Server**, for the **IP address of the Wikipedia Server**.

Once the DNS server provides the IP address (e.g., 208.80.154.224), our browser can use it to connect directly to the **Wikipedia Server** and load the requested web page.

When a user requests a page by entering [**www.wikipedia.org**](http://www.wikipedia.org/) into their browser, the system first checks:

1. **Browser Cache** – If the IP address is stored, it uses it directly.
2. **OS Cache** – If not in the browser cache, the OS checks its local DNS cache.

If the IP address is **not found** in either cache, the system follows the **DNS resolution process** shown in the image:

1. The request is sent to a **DNS server**, which looks up the IP address for www.wikipedia.org.
2. The DNS server **returns the IP address** (208.80.154.224) to the user’s computer.
3. The browser then **connects to the Wikipedia server** using the retrieved IP.
4. The Wikipedia server **responds with the requested webpage**, which is displayed in the browser.

This process ensures that **domain names are translated into IP addresses**, allowing users to access websites without remembering numerical addresses.

![Dns1.svg](/home/reza/Desktop/DNS/Dns1.svg)

### Dns Resolution

**DNS Resolution** is the process of converting a **human-readable domain name** (e.g., www.example.com) into a **machine-readable IP address** (e.g., 93.184.216.34). This process allows browsers and other network devices to locate and communicate with web servers.

### **Example of DNS Resolution**

1. A user types **www.wikipedia.org** in the browser.
2. The browser queries a **DNS server** to find the **IP address** of wikipedia.org.
3. The DNS server responds with the **IP address (208.80.154.224)**.
4. The browser **connects to the Wikipedia server** using the retrieved IP and loads the webpage.

### DNS Resolution Process

When a user types a **domain name** (e.g., www.example.com) into a browser, the system resolves it to an **IP address** through the following steps:

**1. Check Local Cache (Before Querying DNS Servers)**

- **Browser Cache:** Checks if the domain's IP is stored in the browser's cache.
- **OS Cache:** If not found in the browser, the OS checks its local DNS cache.
- **Router Cache:** Some routers maintain a cache of previously resolved domains.

If the IP **is not found** in any cache, the system initiates a **DNS query**.

1. **DNS Query Process (When No Cache Exists)**

The system first contacts a **Recursive DNS Resolver** to find the IP address.

**What is a Recursive DNS Resolver?**

- It is a **DNS server** that helps find the correct IP address for a domain.
- It **performs multiple queries** on behalf of the client until it finds the answer.
- Common **public DNS resolvers** include:
    - **Google DNS** → 8.8.8.8 and 8.8.4.4
    - **Cloudflare DNS** → 1.1.1.1
    - **OpenDNS** → 208.67.222.222

**What Happens in This Step?**

1. The **browser asks the Recursive DNS Resolver**:**"What is the IP address of www.example.com?"**
2. The resolver **checks its cache** to see if it already knows the IP.
    - **If found in cache** → Returns the IP immediately (Fast response).
    - **If not found in cache** → The resolver **queries other DNS servers**:
        - Root Nameserver (.)
        - TLD Nameserver (.com)
        - Authoritative Nameserver (example.com)

### **How the Recursive DNS Resolver Works:**

### ISP Dns Resolver :

An **ISP Resolver** (also called an **ISP DNS Resolver** or **Recursive DNS Resolver from ISP**) is a **DNS server provided by an Internet Service Provider (ISP)** to resolve domain names into IP addresses for its users.

When a user connects to the internet, their ISP automatically assigns a **default DNS resolver** to handle all domain name queries.

When a user requests a website (e.g., www.example.com), the **Recursive DNS Resolver** follows these steps:

1️⃣ **Checks Local Cache**

- First, it looks for the IP address in its **own cache** (previously resolved queries).
- **If found** → Returns the cached IP address.
- **If not found** → Proceeds to query DNS servers.

2️⃣ **Queries the Root Nameserver (.)**

- If no cached result exists, the resolver **contacts a Root Nameserver**.
- Root servers **do not store domain IPs**, but they know where to find **TLD Nameservers**.
- Example Root Servers: a.root-servers.net, b.root-servers.net, etc.

3️⃣ **Queries the Top-Level Domain (TLD) Nameserver**

- The **TLD Nameserver** for .com domains (e.g., a.gtld-servers.net) is contacted.
- The TLD server does **not store the IP** but knows the **Authoritative Nameserver** for example.com.

4️⃣ **Queries the Authoritative Nameserver**

- The **Authoritative Nameserver** for example.com is contacted.
- This server **stores the actual DNS records** and returns the **IP address** of www.example.com.

5️⃣ **Returns the IP Address to the Client**

- The **Recursive DNS Resolver caches the result** for future queries.
- The **IP address is sent to the browser**, which then loads the website.

![dns2.svg](/home/reza/Desktop/DNS/dns2.svg)

### Public DNS Resolver

- **Google DNS (8.8.8.8) and Cloudflare DNS (1.1.1.1) are also Recursive DNS Resolvers.**
- If a user configures their system to use Google DNS, the **query goes to Google’s Recursive Resolver** instead of the ISP’s resolver.
- Google or Cloudflare **then follow the same process** (querying root, TLD, and authoritative servers if needed).

### ISP vs public DNS resolver

| **Feature** | **ISP DNS Resolver** | **Public DNS Resolver (Google, Cloudflare, OpenDNS)** |  |
| --- | --- | --- | --- |
| **Who Provides It?** | Your ISP (Grameenphone, BTCL, etc.) | Google (8.8.8.8), Cloudflare (1.1.1.1), OpenDNS |  |
| **Speed & Reliability** | Can be **slow**, sometimes **censored** | Usually **faster**, more **reliable**, and optimized |  |
| **Security & Privacy** | ISP may **log and track queries** | Google/Cloudflare claim to provide **better privacy** |  |
| **Customization** | **Auto-configured** by ISP | Users can **manually configure** their preferred DNS |  |