# Enterprise Architecture Basics

*Research compiled: 2026-02-20*

## Overview

Enterprise Architecture (EA) is a holistic discipline that defines, organizes, standardizes, and documents an organization's structure and workflows. It creates practical standards across departments to streamline efforts and enable intelligent resource sharing. EA bridges IT and business strategy, ensuring technology investments support and enhance business outcomes.

## Core EA Frameworks

### TOGAF (The Open Group Architecture Framework)

**The TOGAF Standard** is the most widely adopted EA framework globally, centered around the Architecture Development Method (ADM).

#### Key Principle: Information Flow Model

The TOGAF ADM is fundamentally an **information flow model**, not a linear waterfall process. It's inherently incremental and iterative—every activity to develop ADM Phase information constitutes executing that Phase. Enterprise Architects consume inputs and produce mandatory outputs, reusing existing repository knowledge and focusing on gaps.

#### The ADM Phases

The ADM consists of nine core phases (plus a central Requirements Management process):

1. **Preliminary Phase**: Framework & Principles
   - Prepare the organization for successful TOGAF projects
   - Define architecture principles
   - Establish framework and tools

2. **Phase A: Architecture Vision**
   - Define scope and constraints
   - Identify stakeholders
   - Create high-level vision

3. **Phase B: Business Architecture**
   - Develop baseline and target business architecture
   - Map business capabilities and value streams
   - Define business processes and organizational structure

4. **Phase C: Information Systems Architectures**
   - **Data Architecture**: How data is structured, managed, and governed
   - **Application Architecture**: Design and deployment of software applications

5. **Phase D: Technology Architecture**
   - Define hardware, software, and network infrastructure
   - Establish technology standards
   - Plan security architecture

6. **Phase E: Opportunities & Solutions**
   - Identify architecture alternatives
   - Define transition architectures
   - Prioritize implementation projects

7. **Phase F: Migration Planning**
   - Create implementation and migration roadmap
   - Sequence projects
   - Define cost-benefit analysis

8. **Phase G: Implementation Governance**
   - Provide architecture oversight
   - Ensure conformance to target architecture
   - Handle change requests

9. **Phase H: Architecture Change Management**
   - Manage changes to architecture
   - Monitor implementation
   - Ensure architecture remains relevant

**Central Process: Requirements Management**
- Operates continuously throughout all phases
- Manages architecture requirements
- Ensures stakeholder needs are met

#### TOGAF Architecture Domains

TOGAF defines EA work across four primary domains:

1. **Business Architecture**: Strategy, governance, organization, key processes
2. **Information Systems Architecture**: Applications and data
3. **Technology Architecture**: Infrastructure, platforms, networks
4. **Architecture Vision**: Overarching context and scope

### Zachman Framework

**Created by John Zachman** (1987), the Zachman Framework is an enterprise architecture **ontology**—not a methodology. It provides a classification schema for organizing architectural artifacts.

#### Key Distinction: Ontology vs. Methodology

- **Ontology** (Zachman): Defines structure and primitives; unpredictable, producing various outcomes
- **Methodology** (TOGAF, etc.): Defines process and transformation; predictable, repeatable outcomes

Think: Periodic table (ontology) vs. chemical reactions (methodology)

#### The 6×6 Matrix Structure

The Zachman Framework consists of **36 cells** (6 rows × 6 columns):

**Columns (The Interrogatives):**
1. **What** — Data / Things
2. **How** — Function / Processes
3. **Where** — Network / Locations
4. **Who** — People / Organizations
5. **When** — Time / Events
6. **Why** — Motivation / Strategy

**Rows (The Perspectives):**
1. **Planner's View (Scope Contexts)** — Business purpose and strategy
2. **Owner's View (Business Concepts)** — Business model and objectives
3. **Designer's View (System Logic)** — Detailed system design
4. **Builder's View (Technology Physics)** — Implementation details
5. **Subcontractor's View (Component Assemblies)** — Specific components
6. **Enterprise View (Operating Instances)** — Actual functioning system

Each cell represents a unique intersection—for example, "What does the designer need to know about data?" yields a logical data model.

#### Why Zachman?

- Asks fundamental questions (What, How, When, Who, Where, Why)
- Provides comprehensive, composite overview
- Extends to entire enterprise, not just IT
- Assesses completeness of development processes
- Maps stakeholder viewpoints systematically

### Other Notable Frameworks

#### ArchiMate
- **Developed by**: The Open Group
- **Type**: Modeling language for describing EA
- **Focus**: Visual notation and metamodel
- **Integration**: Often used with TOGAF for visualization

#### FEAF (Federal Enterprise Architecture Framework)
- **Developed by**: U.S. Federal Government
- **Context**: Government agencies
- **Scope**: Comprehensive approach across Business, Data, Applications, Technology domains
- **Adoption**: Limited outside federal government

#### DoDAF (Department of Defense Architecture Framework)
- **Developed by**: U.S. Department of Defense
- **Context**: Defense and aerospace industries
- **Focus**: Complex systems, data and people-focused
- **Characteristics**: Mature template for sophisticated EA functions
- **Adoption**: Specialized to defense sector

## The Four Core EA Domains

### 1. Business Architecture

**Definition**: Defines business strategy, governance, organization, and key processes

**Key Components:**
- **Business Strategy**: Strategic direction and objectives
- **Business Capabilities**: Abilities and competencies needed
- **Business Processes**: Key processes and their interrelationships
- **Organizational Structure**: Roles, responsibilities, reporting
- **Business Goals & Objectives**: Measurable targets and outcomes

**Tools & Techniques:**
- Business Process Modeling (BPM)
- Value Stream Mapping (VSM)
- Balanced Scorecard (BSC)
- Capability mapping

**Importance**: Foundation for aligning IT initiatives with business goals; enables effective response to market changes

### 2. Information (Data) Architecture

**Definition**: Organizes, structures, and manages enterprise data

**Key Components:**
- **Data Models**: Structure and relationships
- **Data Governance**: Policies for quality, security, compliance
- **Metadata Management**: Documentation of data assets
- **Data Warehousing & BI**: Centralized analysis and reporting

**Tools & Techniques:**
- Entity-Relationship Diagrams (ERDs)
- Data Flow Diagrams (DFDs)
- Master Data Management (MDM)

**Importance**: Ensures right data reaches right people at right time for informed decision-making

### 3. Application Architecture

**Definition**: Designs, deploys, and manages software applications

**Key Components:**
- **Application Portfolio Management (APM)**: Inventory and lifecycle
- **Service-Oriented Architecture (SOA)**: Service provision and consumption
- **Application Integration**: Seamless communication between systems
- **UI/UX**: User-friendly, effective interfaces

**Tools & Techniques:**
- Unified Modeling Language (UML)
- Enterprise Service Bus (ESB)
- Microservices Architecture

**Importance**: Ensures applications are scalable, maintainable, and support dynamic business needs

### 4. Technology Architecture

**Definition**: Hardware, software, and network infrastructure supporting applications and data

**Key Components:**
- **Infrastructure Services**: Computing, storage, network
- **Technology Standards**: Guidelines for technology selection
- **Security Architecture**: System security and compliance
- **Cloud Computing**: Scalable, flexible IT resources

**Tools & Techniques:**
- Infrastructure as Code (IaC)
- Network diagrams
- Security frameworks
- Cloud platform architectures

**Importance**: Reliable, scalable infrastructure supporting current and future business needs

## Domain Relationships

The four domains form a layered architecture:

```
Environment (external entities and activities)
    ↓
Business Layer (business functions and services)
    ↓
Data Layer (business information and stored data)
    ↓
Information System Layer (business applications and services)
    ↓
Technology Layer (hardware, network, platform services)
```

These domains are **interconnected and interdependent**—effective EA requires cohesive integration across all layers.

## Key Principles

1. **Holistic Approach**: EA considers the entire enterprise, not just IT
2. **Alignment**: IT strategy must align with business strategy
3. **Standardization**: Common standards reduce complexity and cost
4. **Reusability**: Leverage existing architectural assets
5. **Iteration**: Architecture development is iterative, not waterfall
6. **Stakeholder-Centric**: Different stakeholders need different views
7. **Governance**: Continuous oversight ensures architecture compliance

## Evolution and Adoption

Enterprise Architecture emerged in the 1980s (Zachman's seminal 1987 paper) and matured through the 1990s-2000s with TOGAF, FEAF, and DoDAF. Modern EA practice emphasizes:

- **Agility**: EA supports agile development, not hinders it
- **Continuous Architecture**: Ongoing evolution vs. big-bang initiatives
- **Design Thinking Integration**: Human-centered approaches in EA
- **Platform Thinking**: API-first, composable architectures
- **Cloud-Native**: Born-in-cloud architectures replacing legacy lift-and-shift

## Notable Practitioners & Thought Leaders

- **John Zachman**: Creator of Zachman Framework, EA ontology pioneer
- **The Open Group**: Steward of TOGAF Standard
- **Conexiam**: Modern TOGAF interpretation and best practices
- **LeanIX**: EA tooling and framework guidance
- **Gartner**: EA research and advisory

## Sources

- [TOGAF ADM Phases Explained – Conexiam](https://conexiam.com/togaf-adm-phases-explained/)
- [The Zachman Framework – LeanIX](https://www.leanix.net/en/wiki/ea/zachman-framework)
- [Demystifying EA Domains – CIO Portal](https://cioindex.com/reference/enterprise-architecture-domains-explained/)
- [Understanding EA Domains – SnapLogic](https://www.snaplogic.com/blog/understanding-the-four-domains-of-enterprise-architecture)
- [EA Framework Comparison – LeanIX](https://www.leanix.net/en/blog/5-enterprise-architecture-frameworks)
- [Best EA Frameworks – Avolution](https://www.avolutionsoftware.com/news/best-enterprise-architecture-frameworks/)

---

*Next research: Customer Journey Mapping (Phase 2 - Methods/Mapping)*
