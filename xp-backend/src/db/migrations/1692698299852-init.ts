import { MigrationInterface, QueryRunner } from 'typeorm';

export class Init1692698299852 implements MigrationInterface {
  name = 'Init1692698299852';

  public async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.query(
      `CREATE TABLE "observation_view" ("id" SERIAL NOT NULL, "seen_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, "userId" integer NOT NULL, "observationId" integer NOT NULL, CONSTRAINT "PK_eda97c510ac01241ce7250948cf" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_c487360458008645d868ba92d3" ON "observation_view" ("deleted_at") `,
    );
    await queryRunner.query(
      `CREATE TABLE "observation" ("id" SERIAL NOT NULL, "text" text, "tg_photo_id" character varying(256), "tg_document_id" character varying(256), "tg_voice_id" character varying(256), "tg_video_id" character varying(256), "tg_video_note_id" character varying(256), "file_urls" character varying(256) array, "tg_media_group" jsonb array, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, "userId" integer NOT NULL, CONSTRAINT "PK_77a736edc631a400b788ce302cb" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_c485c6aa0770c9895923f47db9" ON "observation" ("created_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_64c2d8c59ee51c0c32a7a42836" ON "observation" ("deleted_at") `,
    );
    await queryRunner.query(
      `CREATE TYPE "public"."experiment_status_enum" AS ENUM('STARTED', 'COMPLETED', 'CANCELED')`,
    );
    await queryRunner.query(
      `CREATE TABLE "experiment" ("id" SERIAL NOT NULL, "text" text, "tg_photo_id" character varying(256), "tg_video_id" character varying(256), "tg_video_note_id" character varying(256), "tg_voice_id" character varying(256), "tg_document_id" character varying(256), "tg_media_group" jsonb array, "geo" jsonb, "status" "public"."experiment_status_enum" NOT NULL DEFAULT 'STARTED', "completed_at" TIMESTAMP WITH TIME ZONE, "complete_by" TIMESTAMP WITH TIME ZONE NOT NULL, "file_urls" character varying(256) array, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, "userId" integer NOT NULL, CONSTRAINT "PK_4f6eec215c62eec1e0fde987caf" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_9ca948c2bcec27a41f177a39a0" ON "experiment" ("status") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_779b5dfa1e540c3749eeb2e3e6" ON "experiment" ("completed_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_fb161369d6daa831f63ff96c61" ON "experiment" ("complete_by") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_b77c18fbb0806d18b3156803b4" ON "experiment" ("created_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_a181b9253bf626ec6d1826304e" ON "experiment" ("deleted_at") `,
    );
    await queryRunner.query(
      `CREATE TABLE "subscription" ("id" SERIAL NOT NULL, "deleted_at" TIMESTAMP WITH TIME ZONE, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "follower_id" integer, "followed_id" integer, CONSTRAINT "PK_8c3e00ebd02103caa1174cd5d9d" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE TABLE "user" ("id" SERIAL NOT NULL, "tg_id" bigint, "username" character varying(32), "password_hash" character(60) NOT NULL, "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, CONSTRAINT "UQ_b49f86c002c69c1203e10bdfcf9" UNIQUE ("tg_id"), CONSTRAINT "UQ_78a916df40e02a9deb1c4b75edb" UNIQUE ("username"), CONSTRAINT "PK_cace4a159ff9f2512dd42373760" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_d091f1d36f18bbece2a9eabc6e" ON "user" ("created_at") `,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_22b81d3ed19a0bffcb660800f4" ON "user" ("deleted_at") `,
    );
    await queryRunner.query(
      `CREATE TABLE "experiment_view" ("id" SERIAL NOT NULL, "seen_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(), "deleted_at" TIMESTAMP WITH TIME ZONE, "userId" integer NOT NULL, "experimentId" integer NOT NULL, CONSTRAINT "PK_ac1576b7871944ed9ab5d849bc7" PRIMARY KEY ("id"))`,
    );
    await queryRunner.query(
      `CREATE INDEX "IDX_5a74b86edae7de58b0fb9daf90" ON "experiment_view" ("deleted_at") `,
    );
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
      `ALTER TABLE "observation_view" ADD CONSTRAINT "FK_8647ee204779b55f21bef4ff4d3" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "observation_view" ADD CONSTRAINT "FK_f67ecb28676c8f29f56b981600b" FOREIGN KEY ("observationId") REFERENCES "observation"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "observation" ADD CONSTRAINT "FK_95e7f729cee52110c1f9a9e719d" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment" ADD CONSTRAINT "FK_efd004fa410567831df8dd764fb" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "subscription" ADD CONSTRAINT "FK_8c37874e2671674e05b6a7ad186" FOREIGN KEY ("follower_id") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "subscription" ADD CONSTRAINT "FK_311b852cec90f8f0a7a78da2164" FOREIGN KEY ("followed_id") REFERENCES "user"("id") ON DELETE NO ACTION ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment_view" ADD CONSTRAINT "FK_b1a58badb56e108cf69b9595994" FOREIGN KEY ("userId") REFERENCES "user"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment_view" ADD CONSTRAINT "FK_642f46c5a429582ad84e5f1dfb2" FOREIGN KEY ("experimentId") REFERENCES "experiment"("id") ON DELETE CASCADE ON UPDATE NO ACTION`,
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
      `ALTER TABLE "experiment_view" DROP CONSTRAINT "FK_642f46c5a429582ad84e5f1dfb2"`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment_view" DROP CONSTRAINT "FK_b1a58badb56e108cf69b9595994"`,
    );
    await queryRunner.query(
      `ALTER TABLE "subscription" DROP CONSTRAINT "FK_311b852cec90f8f0a7a78da2164"`,
    );
    await queryRunner.query(
      `ALTER TABLE "subscription" DROP CONSTRAINT "FK_8c37874e2671674e05b6a7ad186"`,
    );
    await queryRunner.query(
      `ALTER TABLE "experiment" DROP CONSTRAINT "FK_efd004fa410567831df8dd764fb"`,
    );
    await queryRunner.query(
      `ALTER TABLE "observation" DROP CONSTRAINT "FK_95e7f729cee52110c1f9a9e719d"`,
    );
    await queryRunner.query(
      `ALTER TABLE "observation_view" DROP CONSTRAINT "FK_f67ecb28676c8f29f56b981600b"`,
    );
    await queryRunner.query(
      `ALTER TABLE "observation_view" DROP CONSTRAINT "FK_8647ee204779b55f21bef4ff4d3"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_be5b55f18a2f4500881901ad9a"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_ae08ba997167dcefb150433243"`,
    );
    await queryRunner.query(`DROP TABLE "experiment_observations_observation"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_5a74b86edae7de58b0fb9daf90"`,
    );
    await queryRunner.query(`DROP TABLE "experiment_view"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_22b81d3ed19a0bffcb660800f4"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_d091f1d36f18bbece2a9eabc6e"`,
    );
    await queryRunner.query(`DROP TABLE "user"`);
    await queryRunner.query(`DROP TABLE "subscription"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_a181b9253bf626ec6d1826304e"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_b77c18fbb0806d18b3156803b4"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_fb161369d6daa831f63ff96c61"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_779b5dfa1e540c3749eeb2e3e6"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_9ca948c2bcec27a41f177a39a0"`,
    );
    await queryRunner.query(`DROP TABLE "experiment"`);
    await queryRunner.query(`DROP TYPE "public"."experiment_status_enum"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_64c2d8c59ee51c0c32a7a42836"`,
    );
    await queryRunner.query(
      `DROP INDEX "public"."IDX_c485c6aa0770c9895923f47db9"`,
    );
    await queryRunner.query(`DROP TABLE "observation"`);
    await queryRunner.query(
      `DROP INDEX "public"."IDX_c487360458008645d868ba92d3"`,
    );
    await queryRunner.query(`DROP TABLE "observation_view"`);
  }
}
