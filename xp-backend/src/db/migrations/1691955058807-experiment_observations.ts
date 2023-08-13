import { MigrationInterface, QueryRunner } from 'typeorm';

export class ExperimentObservations1691955058807 implements MigrationInterface {
  name = 'ExperimentObservations1691955058807';

  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `CREATE TABLE "experiment_observations_observation" ("experimentId" integer NOT NULL, "observationId" integer NOT NULL, CONSTRAINT "PK_ad7a75d51016c5a162f3de5152c" PRIMARY KEY ("experimentId", "observationId"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_ae08ba997167dcefb150433243" ON "experiment_observations_observation" ("experimentId") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_be5b55f18a2f4500881901ad9a" ON "experiment_observations_observation" ("observationId") `,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment_observations_observation" ADD CONSTRAINT "FK_ae08ba997167dcefb1504332434" FOREIGN KEY ("experimentId") REFERENCES "experiment"("id") ON DELETE CASCADE ON UPDATE CASCADE`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment_observations_observation" ADD CONSTRAINT "FK_be5b55f18a2f4500881901ad9a5" FOREIGN KEY ("observationId") REFERENCES "observation"("id") ON DELETE CASCADE ON UPDATE CASCADE`,
    );
  }

  public async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `ALTER TABLE "experiment_observations_observation" DROP CONSTRAINT "FK_be5b55f18a2f4500881901ad9a5"`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment_observations_observation" DROP CONSTRAINT "FK_ae08ba997167dcefb1504332434"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_be5b55f18a2f4500881901ad9a"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_ae08ba997167dcefb150433243"`,
    );
    await queryRunner.query(`DROP TABLE "experiment_observations_observation"`);
  }
}
