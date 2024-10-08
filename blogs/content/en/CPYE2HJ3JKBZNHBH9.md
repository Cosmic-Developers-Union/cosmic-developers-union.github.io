---
id: CPYE2HJ3JKBZNHBH9
title: Special-Use IP Addresses and Ranges
---

## 1. Loopback Address

- 127.0.0.1 (IPv4)
- ::1 (IPv6)
- localhost Note: Used for internal device communication, always points to itself

## 2. Private Network Addresses

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16## 4. Unique Local Addresses (ULA)
- fc00::/7
- fc00::/8
- fd00::/8## 5. Reserved Addresses
- 0.0.0.0/8
- 240.0.0.0/4 Comment: Reserved for special uses, not assigned to any network.

## 6. Shared Address Space

- 100.64.0.0/10 Comment: Used for Carrier-Grade NAT (CGN).

## 7. Multicast Addresses

- 224.0.0.0/4  
  Comment: Used for one-to-many communication

## 8. Miscellaneous

- \*.local  
  Comment: Used for multicast DNS (mDNS) services

These special addresses and networks are typically used for specific network functions and are not routed on the public internet.
