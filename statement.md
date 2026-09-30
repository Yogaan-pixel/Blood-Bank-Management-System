# Project Statement: Blood Bank Management System

## Problem Statement
Hospitals and healthcare facilities frequently encounter operational bottlenecks when tracking blood stock levels, registering new voluntary donors, and fulfilling emergency blood requests. Relying on manual record-keeping leads to inaccuracies in available inventory, delays in identifying suitable blood matches, and potential shortages during critical hours. A consolidated, real-time management mechanism is essential to reduce administrative delays and match life-saving blood supply with clinical demand swiftly.

## Scope of the Project
This project introduces a terminal-based, local inventory and donor management utility designed for small-scale medical centers, community blood banks, or local clinics. It provides real-time in-memory tracking of blood units categorized by major groups (A+, A-, B+, B-, AB+, AB-, O+, O-) and handles immediate, local records for blood donations and clinical issues. The current implementation is scoped to run within a single session using standard console input/output and structured in-memory data tables without external database dependencies.

## Target Users
* **Blood Bank Administrators & Staff:** Clerical operators responsible for entering daily donation data, updating warehouse volumes, and adjusting stock balances.
* **Clinic Coordinators:** Healthcare workers needing to check immediate blood availability before initiating medical procedures or scheduling patient transfers.
* **Inventory Managers:** Logistics staff tasked with verifying existing volumes across various blood types to monitor against expiration or run-out metrics.

## High-Level Features
* **Donor Directory Management:** Collects and displays unique donor registration details including full names, ages, blood group classifications, and phone contacts.
* **Real-Time Inventory Auditing:** Displays current stock tracking matrices across all major blood types with instant balance incrementing and decrementing adjustments.
* **Automated Allocation Checks:** Validates requested blood groups and unit availability during issue requests to prevent accidental over-allocation or stock deficits.
* **Interactive Command Menu:** Provides a guided, input-validated numerical console menu interface ensuring users can navigate system features cleanly without operational errors.
