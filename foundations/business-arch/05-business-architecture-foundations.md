# Business Architecture Foundations

*Research Date: 2026-02-19*
*Topic: Business Architecture BIZBOK capability mapping value streams business model*

## Overview

Business architecture provides a clear roadmap for organizations by analyzing and designing business processes, functions, and structures. It creates a blueprint that explains how a business operates, identifies areas for improvement, defines rules and guidelines, and aligns all activities with overall strategy.

Unlike enterprise architecture (which takes a broader view including technology), business architecture focuses strictly on business functions and their optimization.

## Core Framework: BIZBOK®

The Business Architecture Body of Knowledge (BIZBOK®) is the definitive framework maintained by the Business Architecture Guild. It consolidates best practices, principles, and techniques into an overall framework for business architecture practice.

**Key Publication:**
- BIZBOK® Guide (current version 10.0+, regularly updated)
- Maintained by Business Architecture Guild
- Industry-specific reference models available to members (~$150/year)

**Sources:**
- https://www.businessarchitectureguild.org/
- https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/bizbok_10/introduction_v10_final.pdf

---

## Core Domains of Business Architecture

According to BIZBOK®, business architecture consists of interconnected domains that provide different perspectives on organizational structure and operations:

### 1. **Value Streams**

Value streams represent end-to-end collections of value-adding activities that create a result for a stakeholder (customer or another stakeholder).

**Key Characteristics:**
- Customer-initiated or commonly engaged flows
- Consist of discrete **value stream stages**
- Each stage adds incremental stakeholder value
- Represent *what* the business needs to do from a value-delivery perspective
- Business architecture views value stream stages as **collections of capabilities**

**Relationship to Process:**
- Value streams are *strategic* and stable (the "what")
- Business processes are *operational* implementations (the "how")
- One value stream can map to multiple process variants

**Starting Point:** The recommended business architecture baseline includes commonly engaged and customer-initiated value streams.

**Sources:**
- https://pubs.opengroup.org/togaf-standard/business-architecture/value-streams.html
- https://bizarchmastery.com/straighttalk/value-mindset-demystifying-business-architecture-value-stream
- https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/bpm_paper_final_dec2019.pdf

### 2. **Capabilities**

Business capabilities represent an organization's **capacity and ability to deliver value**—what an organization can do, independent of how, who, or where.

**Key Characteristics:**
- Define *what* the business can do (not *how* it's done)
- Technology-agnostic and organization-agnostic
- Stable over time (even as processes change)
- Typically organized in a hierarchical map (2-3 levels deep)
- There can be **only one capability map** for an organization

**Capability vs. Process:**
| **Capability** | **Process** |
|----------------|-------------|
| What the business can do | How work gets done |
| Stable, strategic | Changes with optimization |
| Technology-independent | Often technology-specific |
| Defines potential | Defines execution |

**Capability Mapping Best Practices:**
1. Focus on what's necessary for useful insight—don't overcomplicate hierarchy
2. Distinguish **core capabilities** (competitive differentiation) from **non-core** (outsourcing candidates)
3. Use heat maps to visualize maturity, performance, or investment
4. Align capabilities to value stream stages to show dependency

**Value Stream / Capability Cross-Mapping:**
This blueprint shows which capabilities enable each value stream stage—one of the most critical BA artifacts. As BIZBOK® notes: *"Business capabilities alone are not enough... there [must be] a clear view of stakeholder engagement and how stakeholder value will be achieved."*

**Sources:**
- https://www.ardoq.com/knowledge-hub/business-capability-modeling
- https://www.leanix.net/en/wiki/ea/business-capability
- https://pubs.opengroup.org/togaf-standard/business-architecture/business-capabilities.html
- https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/whitepapers/business_architecture_metamo.pdf

### 3. **Information**

Business architecture identifies the types of information required, and how information is captured, stored, processed, and shared across the organization. This includes:

- **Information concepts** (business-level data entities)
- Information flows between capabilities and value stream stages
- Information lifecycle management

**Key Point:** BIZBOK® focuses on business-level information mapping, not detailed data models or system schemas—that's the domain of data architecture.

### 4. **Organization**

The organizational domain maps structure, roles, and responsibilities:

- Organizational units and hierarchy
- Roles and accountabilities
- Stakeholder groups
- Relationship to capabilities (who performs what)

---

## Key Relationships

### Value Streams ↔ Capabilities

**Critical Principle:** Value streams and capabilities inform and validate each other.

- **Value stream stages** describe the *sequence* of activities needed
- **Capabilities** describe whether the business *can perform* those activities to the needed level
- The cross-mapping reveals gaps, redundancies, and dependencies

**From BIZBOK®:**
> "Business capabilities are identified through a business's value streams, and there can only be one set of capabilities for each [organization]."

**TOGAF reinforcement:**
> "Value streams are not capabilities, nor components of capabilities... they specifically describe the sequence of activities that the business needs to undertake to produce or realize value."

### Process ↔ Capabilities

- A **process activity** is an instance of a **capability instance**
- Processes operationalize capabilities
- Multiple processes may leverage the same capability

**Sources:**
- https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/bpm_paper_final_dec2019.pdf
- https://bizzdesign.com/blog/business-architect-toolbox-stream-mapping

---

## Business Models

Business models define how an organization creates, delivers, and captures value:

- Revenue streams
- Target customer segments
- Key activities and resources
- Partnerships required to sustain the business
- Value propositions

A well-defined business model helps identify opportunities, adapt to market changes, and drive innovation.

**Source:**
- https://bizzdesign.com/blog/what-is-business-architecture

---

## Frameworks & Standards

### BIZBOK® Guide (Business Architecture Guild)

**Purpose:** Codify best practices for business architecture discipline

**Key Elements:**
- Core metamodel (value streams, capabilities, information, organization)
- Guiding principles and techniques
- Knowledgebase approach (practitioner-led)
- Industry reference models (banking, healthcare, insurance, etc.)

**Certification:** Business Architecture Guild offers CABA (Certified Business Architect) certification based on BIZBOK®.

**Resources:**
- Main site: https://www.businessarchitectureguild.org/
- Membership: ~$150/year for industry models and full BIZBOK® access
- White papers available: https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/

### TOGAF® (The Open Group Architecture Framework)

**TOGAF 10** incorporated business architecture concepts aligned with BIZBOK®, including:

- Business capability modeling
- Value stream mapping
- Integration with enterprise architecture (ADM phases)

**Key TOGAF Business Architecture Guides:**
- TOGAF® Series Guide: Business Capabilities
- TOGAF® Series Guide: Value Streams

**Note:** TOGAF explains BA concepts but doesn't detail them as comprehensively as BIZBOK®. TOGAF stays at the business layer and doesn't dive into systems/technology (unlike full EA frameworks).

**Sources:**
- https://pubs.opengroup.org/togaf-standard/business-architecture/
- https://www.reddit.com/r/EnterpriseArchitect/comments/1i9ra4h/ (practitioner discussion on TOGAF vs. BIZBOK)

### ArchiMate® & BIZBOK® Mapping

ArchiMate® (The Open Group modeling language) and BIZBOK® metamodels have been mapped to enable visual modeling of business architectures. Bizzdesign and others provide tooling that bridges both standards.

**Source:**
- https://bizzdesign.com/blog/business-architecture-redefined-mapping-bizbokr-archimater

---

## Practical Application

### How to Engage in Business Architecture

1. **Identify starting scope:**
   - Customer-initiated value streams
   - Core capabilities
   - Critical information flows

2. **Assemble cross-functional SMEs:**
   - Same group for both value streams and capabilities
   - Can define both during same work sessions

3. **Create baseline artifacts:**
   - Capability map (hierarchical, 2-3 levels)
   - Value stream map (end-to-end flows)
   - Information map (key concepts)

4. **Cross-map and analyze:**
   - Value stream stages → capabilities
   - Capabilities → applications (with EA/IT)
   - Identify gaps, redundancies, misalignments

5. **Prioritize and plan:**
   - Heat maps for capability maturity
   - Roadmap for improvements
   - Align initiatives to strategy

### Aligning Business Architecture with Strategy

Business architecture helps organizations:

- **Translate strategy into execution:** Decompose strategic goals into required capabilities
- **Identify capability gaps:** Compare current vs. required capability maturity
- **Prioritize investments:** Focus on capabilities that enable strategic value streams
- **Enable transformation:** Provide stable foundation during organizational change
- **Improve decision-making:** Provide context for IT investments, M&A, outsourcing

**Source:**
- https://www.capstera.com/business-architecture-value-streams/

---

## Use Cases & Benefits

### Strategic Planning
- Align business units with overall strategy
- Identify which capabilities drive competitive advantage
- Support make-vs-buy and outsourcing decisions

### Operating Model Design
- Define target operating models based on capability architecture
- Support org design aligned to value delivery
- Enable shared services and centers of excellence

### Digital Transformation
- Map legacy systems to business capabilities
- Prioritize modernization based on capability criticality
- Design future-state architecture

### Merger & Acquisition
- Compare capability portfolios of merged entities
- Identify redundancies and synergies
- Plan integration roadmaps

**Sources:**
- https://www.avolutionsoftware.com/news/the-benefits-of-business-capability-models-for-enterprise-architects/
- https://kotusev.com/Modeling%20Business%20Capabilities%20in%20Enterprise%20Architecture%20Practice%20-%20The%20Case%20of%20Business%20Capability%20Models.pdf

---

## Distinction: Business Architecture vs. Enterprise Architecture

| **Business Architecture** | **Enterprise Architecture** |
|---------------------------|----------------------------|
| Focus: Business functions, processes, capabilities | Focus: Entire organization (business + technology + data) |
| Scope: Value delivery and operating model | Scope: Holistic alignment across all domains |
| Technology: Agnostic (what, not how) | Technology: Includes application and infrastructure layers |
| Audience: Business leaders, COO, strategy | Audience: CIO, CTO, architects, IT leadership |
| Frameworks: BIZBOK® | Frameworks: TOGAF, Zachman, FEAF |

**Integration Point:** Business architecture provides the *business context* layer for enterprise architecture. EA builds on BA by adding application, data, and technology architecture layers.

**Source:**
- https://bizzdesign.com/blog/what-is-business-architecture

---

## Notable Practitioners & Resources

### Organizations
- **Business Architecture Guild** – Primary professional body, maintains BIZBOK®
- **The Open Group** – Publishes TOGAF and ArchiMate standards
- **OMG (Object Management Group)** – Publishes Value Delivery Metamodel

### Key Practitioners & Thought Leaders
- **William Ulrich** – Co-author of foundational BA papers, Guild leader
- **Jim Rhyne** – Business architecture pioneer
- **Bizzdesign** – Tooling vendor, educational content
- **LeanIX** – SaaS EA platform with BA capabilities
- **Capstera** – Pre-built business architecture models

### Academic Research
- **Kotusev & Alwadain (2023):** "Modeling Business Capabilities in Enterprise Architecture Practice"
  - Identified 9 general BA modeling approaches in practice
  - First systematic study of capability model usage
  - Published in *Information Systems Management*, Vol 41, No 2

**Sources:**
- https://www.tandfonline.com/doi/full/10.1080/10580530.2023.2231635

---

## Key Takeaways

1. **Business architecture is strategic, not operational:** It defines *what* an organization does (capabilities, value streams) independent of *how* it does it (processes, systems).

2. **BIZBOK® is the definitive framework:** Maintained by the Business Architecture Guild, it's the industry standard for BA practice.

3. **Four core domains:** Value Streams, Capabilities, Information, Organization—all interconnected.

4. **Value Stream / Capability cross-mapping is essential:** This relationship reveals how the organization delivers value and where gaps exist.

5. **Business architecture bridges strategy and execution:** It translates high-level goals into concrete capabilities and provides a stable foundation for transformation.

6. **Capabilities are stable; processes change:** This separation enables organizations to evolve operations without constant strategic disruption.

7. **BA is the business layer of EA:** Enterprise architecture builds on business architecture by adding technology, application, and infrastructure layers.

---

## Next Topics to Explore

- **Service Blueprinting** and its relationship to value stream mapping
- **Capability-based planning** methodologies
- **Business operating models** and how BA informs org design
- **ArchiMate notation** for visualizing business architectures
- **Agile and SAFe integration** with business architecture

---

## Sources

1. Business Architecture Guild – BIZBOK® Guide: https://www.businessarchitectureguild.org/
2. TOGAF Business Architecture: https://pubs.opengroup.org/togaf-standard/business-architecture/
3. Bizzdesign BA Resources: https://bizzdesign.com/blog/what-is-business-architecture
4. LeanIX Capability Model Guide: https://www.leanix.net/en/wiki/ea/business-capability
5. Ardoq BA Knowledge Hub: https://www.ardoq.com/knowledge-hub/business-capability-modeling
6. Capstera Value Streams Guide: https://www.capstera.com/business-architecture-value-streams/
7. BMC BIZBOK Introduction: https://www.bmc.com/blogs/bizbok-introduction/
8. Kotusev & Alwadain (2023): https://www.tandfonline.com/doi/full/10.1080/10580530.2023.2231635
9. Business Architecture Guild White Papers: https://cdn.ymaws.com/www.businessarchitectureguild.org/resource/resmgr/public_resources/
10. BizArch Mastery (practitioner blog): https://bizarchmastery.com/

---

*Curated by Guran 🗡️ | Part of Service Design × Business Architecture knowledge base*
