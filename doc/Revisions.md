# Revisions

## Final Revisions
Included with Stage 4 Release.

To reflect changes in Sessions entity:
- In `DatabaseDesign.md`:
  - Updated database design diagram (`img/database_design_diagram_v3.png`).
  - Updated Sessions entity description and its 3NF normalization.
- In `DatabaseImplementationIdx.md`:
  - Updated table creation command for Sessions.

## Revisions for Stage 3
Included with Stage 3 Revisions Release.

- Revised indexing section for query 3 and query 4 to exclude primary key from consideration for indexing trials.

## Revisions for Stage 2
Included with Stage 3 Release.

- Updated database design diagram (`img/database_design_diagram_v2.png`) to use weak entity syntax for Weather, OceanSpecies, and NaturalDisaster since their primary keys are also foreign keys from the Regions entity.
  - Updated attributes to align with Stage 3.

## Revisions for Stage 1
Included with Stage 2 Release.

- Updated Technical Challenges section to discuss the creative ways in which we may need to design our database.
  - To summarize, we anticipate facing challenges in defining the design of our app components in order to manage our database efficiently.